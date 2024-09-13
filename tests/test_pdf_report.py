import os
from unittest.mock import MagicMock
from pdf_report import FileSharer, PdfReport
from dotenv import load_dotenv

load_dotenv()

class TestPdfReport:

    def test_instance_pdf_report(self):
        test_pdf_report = PdfReport("test_filename.pdf")
        assert test_pdf_report.filename == "test_filename.pdf"

    def test_generate(self, mocker):
        mock_webbrowser = mocker.patch("pdf_report.webbrowser.open")
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
        
        mock_webbrowser.assert_called_once_with("file://" + os.path.realpath(f"files/test_report.pdf"))


class TestFileSharer:
    
    def test_share(self, mocker):
        
        mock_client = mocker.patch("pdf_report.Client")
        
        mock_filelink = MagicMock()
        mock_filelink.url = "http://example.com/sharedfile"
        
        mock_client.return_value.upload.return_value = mock_filelink
        
        sharer = FileSharer(filepath="testfile.txt")
        
        result = sharer.share()
        
        assert result == "http://example.com/sharedfile"
        
        mock_client.assert_called_once_with(os.getenv("FILESTACK_API_KEY"))
        
        mock_client.return_value.upload.assert_called_once_with(filepath="testfile.txt")