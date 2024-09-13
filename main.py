from bill import Bill
from flatmate import Flatmate
from pdf_report import FileSharer, PdfReport
from pathlib import Path

def main():
    amount = float(input("Hello user, what is the total bill amount to split? "))
    period = input("What is the period for the bill to split? E.g. January 2025: ")
    flatmate1_name = input("What is your name? ")
    flatmate2_name = input("What is your flatmate's name? ")
    flatmate1_days_in_house = int(input("How many days have you been in the house? "))
    flatmate2_days_in_house = int(input(f"How many days has {flatmate2_name} been in the house? "))
    
    bill = Bill(amount, period)
    flatmate1 = Flatmate(flatmate1_name, flatmate1_days_in_house)
    flatmate2 = Flatmate(flatmate2_name, flatmate2_days_in_house)

    print(f"{flatmate1.name} pays: £{flatmate1.pays(bill, flatmate2)}")
    print(f"{flatmate2.name} pays: £{flatmate2.pays(bill, flatmate1)}")

    pdf_report = PdfReport(filename=f"{bill.period}.pdf")
    pdf_report.generate(flatmate1, flatmate2, bill)
    
    directory = Path("files")
    
    file_sharer = FileSharer(filepath=directory / pdf_report.filename)
    print(file_sharer.share())

if __name__ == "__main__":
    main()
