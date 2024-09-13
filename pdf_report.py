import os
import webbrowser
from fpdf import FPDF
from filestack import Client
from dotenv import load_dotenv

load_dotenv()

class PdfReport:
    """
    Creates a PDF file that contains data about
    the flatmates, such as their names, their due 
    amount, and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        # Add image
        pdf.image(name="files/house.png", w=50, h=50)

        # Add title
        pdf.set_font(family='Arial', size=32, style="B")
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=0, align="C", ln=1)

        # Add Bill Period
        pdf.set_font(family='Arial', size=24, style="B")
        pdf.cell(w=0, h=50, txt=f"Bill Month: {bill.period}", border=0, ln=1)

        # Add flatmates' payments
        pdf.set_font(family='Arial', size=16)
        flatmate1_payment = flatmate1.pays(bill=bill, flatmate2=flatmate2)
        flatmate2_payment = flatmate2.pays(bill=bill, flatmate2=flatmate1)

        pdf.cell(
            w=0, 
            h=30, 
            txt=f"{flatmate1.name} pays £{flatmate1_payment} for {flatmate1.days_in_house} days.", 
            border=0, 
            ln=1
        )
        pdf.cell(
            w=0, 
            h=30, 
            txt=f"{flatmate2.name} pays £{flatmate2_payment} for {flatmate2.days_in_house} days.", 
            border=0, 
            ln=1
        )

        # Output the PDF
        pdf.output(f"files/{self.filename}", 'F')
        webbrowser.open("file://" + os.path.realpath(f"files/{self.filename}"))
        
        
class FileSharer:
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.api_key = os.getenv("FILESTACK_API_KEY")
        
    def share(self):
        client = Client(self.api_key)
        
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url