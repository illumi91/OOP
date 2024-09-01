from bill import Bill
from flatmate import Flatmate
from pdf_report import PdfReport

def main():
    bill = Bill(amount=120, period="March 2021")
    john = Flatmate(name="John", days_in_house=20)
    marry = Flatmate(name="Marry", days_in_house=25)

    print(f"{john.name} pays: £{john.pays(bill=bill, flatmate2=marry)}")
    print(f"{marry.name} pays: £{marry.pays(bill=bill, flatmate2=john)}")

    pdf_report = PdfReport(filename="march_bill.pdf")
    pdf_report.generate(flatmate1=john, flatmate2=marry, bill=bill)

if __name__ == "__main__":
    main()
