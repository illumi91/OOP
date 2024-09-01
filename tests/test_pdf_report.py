from unittest.mock import MagicMock
from pdf_report import PdfReport

class TestPdfReport:

    def test_instance_pdf_report(self):
        test_pdf_report = PdfReport("test_filename.pdf")
        assert test_pdf_report.filename == "test_filename.pdf"

    def test_generate(self, mocker):
        pdf_report = PdfReport("test_report.pdf")

        mock_pdf = mocker.patch("pdf_report.FPDF", autospec=True)
        mock_instance = mock_pdf.return_value

        flatmate1 = MagicMock()
        flatmate2 = MagicMock()
        bill = MagicMock()

        flatmate1.pays.return_value = 100
        flatmate2.pays.return_value = 150

        flatmate1.name = "Flatmate1"
        flatmate1.days_in_house = 20
        flatmate2.name = "Flatmate2"
        flatmate2.days_in_house = 25
        bill.period = "January 2024"

        pdf_report.generate(flatmate1, flatmate2, bill)
        
        mock_instance.add_page.assert_called_once()
        mock_instance.image.assert_called_once_with(name="files/house.png", w=50, h=50)
        mock_instance.set_font.assert_any_call(family='Arial', size=32, style="B")
        mock_instance.cell.assert_any_call(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)
        mock_instance.cell.assert_any_call(w=0, h=50, txt="Bill Month: January 2024", border=0, ln=1)
        mock_instance.cell.assert_any_call(w=0, h=30, txt="Flatmate1 pays £100 for 20 days.", border=0, ln=1)
        mock_instance.cell.assert_any_call(w=0, h=30, txt="Flatmate2 pays £150 for 25 days.", border=0, ln=1)
        mock_instance.output.assert_called_once_with("files/test_report.pdf", 'F')

        