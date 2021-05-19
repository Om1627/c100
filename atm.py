class atm(object):
    def __init__(self, cardnumber, pin):
        self.cardnumber=cardnumber
        self.pin=pin
        
    def main(self):
        accNo=input("Enter your account number ")
        pin=input("Enter your pin ")

    
    def CashWithdrawl(self):
        
       amount=int(input("Enter amount of cash to be withdrawed "))
       newamount=2000-amount
       print("You have withdrawed ",amount,"Your remaining balance is ",newamount)

    def balanceEnquiry(self):
        print("Your account balance is 2000 ")

   
Atm=atm(12345678,1234)
Atm.main()
x=int(input("Type 1 for withdrawing cash and 2 for balance enquiry "))
if(x==1):
    Atm.CashWithdrawl()
else:
    print(Atm.balanceEnquiry())    