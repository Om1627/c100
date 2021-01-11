class atm(object):
    def __init__(self, cardnumber, pin):
        self.cardnumber=cardnumber
        self.pin=pin
        

    def CashWithdrawl(self,amount):
       amount=input("Enter amount of cash to be withdrawed ")
       print("Cash withdrawed ",amount)

    def balanceEnquiry(self):
        print("Your account balance is 2000 ")

   
Atm=atm(12345678,1234)
print(Atm.CashWithdrawl(0))
