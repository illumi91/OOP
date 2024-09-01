from bill import Bill
from flatmate import Flatmate

class TestFlatmate():
    
    def test_instance_flatmate(self):
        flatmate = Flatmate("ciccio", 20)
        
        assert flatmate.name == "ciccio"
        assert flatmate.days_in_house == 20
        
    def test_pays_non_zero_total_days(self):
        flatmate = Flatmate("ciccio", 20)
        flatmate2 = Flatmate("ciccio2", 25)
        bill = Bill(120, "January 1991")
        
        flatmate_pay = flatmate.pays(bill=bill, flatmate2=flatmate2)
        
        assert flatmate_pay == round(120 * (20 / 45), 2)
        
    def test_pays_zero_total_days(self):
        flatmate = Flatmate("ciccio", 0)
        flatmate2 = Flatmate("ciccio2", 0)
        bill = Bill(120, "January 1991")
        
        flatmate_pay = flatmate.pays(bill=bill, flatmate2=flatmate2)
        
        assert flatmate_pay == 0
        
    def test_flatmate_pays_zero_zero_days(self):
        flatmate = Flatmate("ciccio", 0)
        flatmate2 = Flatmate("ciccio2", 20)
        bill = Bill(120, "January 1991")
        
        flatmate_pay = flatmate.pays(bill=bill, flatmate2=flatmate2)
        flatmate2_pay = flatmate2.pays(bill=bill, flatmate2=flatmate)
        
        assert flatmate_pay == 0
        assert flatmate2_pay == 120
        
    def test_flatmates_pays_same_amount(self):
        flatmate = Flatmate("ciccio", 20)
        flatmate2 = Flatmate("ciccio2", 20)
        bill = Bill(120, "January 1991")
        
        flatmate_pay = flatmate.pays(bill=bill, flatmate2=flatmate2)
        flatmate2_pay = flatmate2.pays(bill=bill, flatmate2=flatmate)
        
        assert flatmate_pay == 60
        assert flatmate2_pay == 60
        
    def test_flatmate_pays_zero_zero_amount(self):
        flatmate = Flatmate("ciccio", 25)
        flatmate2 = Flatmate("ciccio2", 20)
        bill = Bill(0, "January 1991")
        
        flatmate_pay = flatmate.pays(bill=bill, flatmate2=flatmate2)
        flatmate2_pay = flatmate2.pays(bill=bill, flatmate2=flatmate)
        
        assert flatmate_pay == 0
        assert flatmate2_pay == 0       
        
        