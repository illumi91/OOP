from bill import Bill

class TestBill:
    
    def test_instance_bill(self):
        test_bill = Bill(3, "January 1991")
        
        assert test_bill.amount == 3
        assert test_bill.period == "January 1991"
    