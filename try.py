class Employee:
    def __init__(self):
        self.income = 0
        self.__tax = 0

    def earn_money(self, money):
        self.income += money
        self.__tax += self.income * 0.05

    def get_tax(self):
        return self.__tax

    @property
    def tax_amount(self):
        return self.income * 0.05


Terry = Employee()
Terry.earn_money(300)
print(Terry.tax_amount)
