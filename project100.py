class Atm(object):
    def __init__(self,cardNumber,pinNumber):
        self.card_numbeer=cardNumber,
        self.pin_number=pinNumber
    def CashWithdrawl(self):
        print("cash withdrawled")
    def BalanceEnquiry(self):
        print("balance enquired")
    def checkbook(self):
        print("checkbook deposited")
        print("checkbook returned")
    def pinGeneration(self):
        print("your pin is generated")
atm1=Atm("113T3NVSVSFBs","1234")
atm1.BalanceEnquiry()
atm1.pinGeneration()
atm1.checkbook()
atm1.CashWithdrawl()