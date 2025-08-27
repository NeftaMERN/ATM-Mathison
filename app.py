
class ATM:

    def __init__(self, balanc=100):
        self.balanc = balanc
    
    def show_balanc(self):
        print(f'Curent balanc {self.balanc}')
    
    def Deposit(self, amount=None):
        if amount is None:
            amount = int(input('Enter amount: '))
        self.balanc += amount
        print(f'You Deposit {amount} curent balanc {self.balanc}')
    
    def withdraw(self, amount=None):
        if amount is None:
            amount = int(input('Enter amount: '))
        self.balanc -= amount
        print(f'You withdraw {amount}, Curent balance {self.balanc}')

    def manu(self):
        while True:
            print("\n--- ATM Menu ---")
            print('1.Show balanc')
            print('2.Deposit')
            print('3.withdraw')
            print("4. Exit")
            choice = input("Choose one: ")

            if choice == '1':
                self.show_balance()
            elif choice == '2':
                self.deposit()
            elif choice == '3':
                self.withdraw()
            elif choice == '4':
                print("Exiting... Thank you for using the ATM!")
                break
            else:
                print("Invalid choice, try again.")

atm1 = ATM()
atm1.menu()