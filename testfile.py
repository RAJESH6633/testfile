class bank():
    Bankname='sbi'
    nobranches=100
    ROI=0.9
    def __init__(self,name,mno,mail,aadhaarno,pan,accno,bal,pin):
        self.name=name
        self.mno=mno
        self.mail=mail
        self.aadhaarno=aadhaarno
        self.pan=pan
        self.accno=accno
        self.bal=bal
        self.pin=pin
    def checkbal(self):
        if self.pin==self.getpin():
            print(f' {self.name} account balance is {self.bal}')
        else:
            print('the pin is incorrect')
    def deposite(self,amount):
        self.bal+=amount
        print(f'amount is credired successfully...!')
        print(f'available balance is {self.bal}')
    def withdraw(self,amount):
        if self.pin==self.getpin():
            if self.bal>=amount:
                self.bal-=amount
                print("amount is debited successfully in:",{self.accno},"and available balance is:",{self.bal})
            else:
                print("insufficient balance")
        else:
            print("incorrect pin")
    @classmethod
    def changeROI(cls,n):
        cls.ROI=n
        print('the rate of interest is changed')
    @staticmethod
    def getpin():
        return int(input('enter 4 digits pin: '))

obj=bank('ram',1234567890,'rajesh@1234',456824706777,'RMPLB5848D',320017001,100000,1122)

obj.deposite(2000)
obj.checkbal()
obj.withdraw(1122,3000)
 cls.ROI(0.7)




