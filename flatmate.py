class Flatmate:
    """
    Represents a flatmate who lives in the flat 
    and pays a share of the bill.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        total_days = self.days_in_house + flatmate2.days_in_house
        if total_days == 0:
            return 0
        weight = self.days_in_house / total_days
        return round(bill.amount * weight, 2)
