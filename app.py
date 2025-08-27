
class ATM:

    def __init__(self, balance=100, PIN=1234, account_number = 1111):
        self.balance = balance
        self.PIN = PIN
        self.account_number = account_number
    
    def show_balance(self):
        print(f'Curent balance {self.balance}')
    
    def deposit(self, amount=None):
        if amount is None:
            amount = int(input('Enter amount: '))
        self.balance += amount
        print(f'You Deposit {amount} curent balanc {self.balance}')
    
    def withdraw(self, amount=None):
        if amount is None:
            amount = int(input('Enter amount: '))
        self.balance -= amount
        print(f'You withdraw {amount}, Curent balance {self.balance}')

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
    
    def authenticate(self):
        entered_acc = input('Enter account number: ')
        entered_pin = input('Enter PIN: ')

        if entered_acc == self.account_number and entered_pin == self.PIN:
            print('Login successful')
            self.manu()
        else:
            print("Wrong account number or PIN! Access denied.")

atm1 = ATM(balance=500, PIN="9999", account_number="123456")
atm1.authenticate()
