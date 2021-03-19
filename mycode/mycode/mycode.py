def place_value(number): 
    return ("{:,}".format(number))

class company:
    def __init__(self, name, price, shares, book_price):
        self.price=price
        self.shares=shares
        self.book_price=book_price
        self.company_val=self.book_price*self.shares
        self.market_capitalization=self.price*self.shares

    def dividend(self, dividend):
        self.price=self.price-dividend
        self.book_price=self.book_price-dividend
        self.company_val=self.book_price*self.shares
        self.market_capitalization=self.price*self.shares

    def bonus(self,percentage):
        self.shares=self.shares+((self.shares/100)*percentage)
        self.price=(self.price/(100+percentage))*(100)
        self.book_price=self.book_price/(100+percentage)*(100)

    def report(self):
        print("")
        print("   \\\\\\ COMPANY REPORT /////")
        print("")
        print("   Price: ",place_value(self.price))
        print("   Shares: ",place_value(self.shares))
        print("   Market Capitalization: ",place_value(self.market_capitalization))
        print("   Book Price: ",place_value(self.price))
        print("   Company Value: ",place_value(self.company_val))
        print("\n")


company1=company("STN Bank",100,100,100)
company1.report()
company1.dividend(5)
company1.report()
company1.bonus(900)
company1.report()