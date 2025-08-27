
class ATM:

    def __init__(self, balanc=100):
        self.balanc = balanc
    
    def show_balanc(self):
        print(self.balanc)
    

atm1 = ATM()
atm1.show_balanc()