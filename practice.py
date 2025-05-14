class Atm:

    def __init__(self):
        print(f"ATM Object created. ID: {id(self)}")
        self.pin = ''
        self.balance = 0
        self.menu()

    def menu(self):
        while True:
            print("""
            Hi, how can I help you?
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Press 5 to exit
            """)
            user_input = input("Choose an option: ")

            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.change_pin()
            elif user_input == '3':
                self.check_balance()
            elif user_input == '4':
                self.withdraw()
            elif user_input == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

    def create_pin(self):
        user_pin = input('Enter your new pin: ')
        self.pin = user_pin
        try:
            user_balance = int(input('Enter initial balance: '))
            self.balance = user_balance
            print('Pin created successfully.')
        except ValueError:
            print("Invalid input. Balance should be a number.")
        
    def change_pin(self):
        old_pin = input('Enter old pin: ')

        if old_pin == self.pin:
            new_pin = input('Enter new pin: ')
            self.pin = new_pin
            print('Pin change successful.')
        else:
            print('Incorrect old pin. Try again.')

    def check_balance(self):
        user_pin = input('Enter your pin to check balance: ')
        if user_pin == self.pin:
            print(f'Your balance is {self.balance}')
        else:
            print('Incorrect pin. Access denied.')

    def withdraw(self):
        user_pin = input('Enter your pin to withdraw: ')
        if user_pin == self.pin:
            try:
                amount = int(input('Enter the amount to withdraw: '))
                if amount <= self.balance:
                    self.balance -= amount
                    print(f'Withdrawal successful. Remaining balance: {self.balance}')
                else:
                    print('Insufficient funds.')
            except ValueError:
                print("Invalid input. Amount should be a number.")
        else:
            print('Incorrect pin. Access denied.')

if __name__ == "__main__":
    atm = Atm()
