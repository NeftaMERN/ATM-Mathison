
class ATM:

    def __init__(self, balanc=100):
        self.balanc = balanc
    
    def show_balanc(self):
        print(self.balanc)
    
    def Deposit(self, amount):
        self.balanc += amount
        print(f'You Deposit {amount} curent balanc {self.balanc}')

atm1 = ATM()
atm1.Deposit(100)