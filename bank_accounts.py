class balance_exception(Exception):
    pass


class BankAccount:
    def __init__(self, initial_ammount, account_name):
        self.balance = initial_ammount
        self.name = account_name
        print(
            f"\nAccount '{self.name}' created. \nBalance = UGX{self.balance:.2f}")

    def get_balance(self):
        print(f"\nAccount '{self.name}' Balance = UGX{self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete.")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise balance_exception(
                f"\nSorry, Accooutn '{self.name}' only has a balance of UGX{self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw Successful")
            self.get_balance()
        except balance_exception as error:
            print(f"\nWithdraw Interrupted {error}")

    def transfer(self, amount, account):
        try:
            print('\n***********\nBeginning Transaction.....🚀')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('\nTransaction Successful!✅ \n\n*********')
        except balance_exception as error:
            print(f'Transaction Unsuccessful.  ❌ {error}')


class Interest_rewards_account(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print('\nDeposit Complete.')
        self.get_balance()


class Savings_account(Interest_rewards_account):
    def __init__(self, initial_ammount, account_name):
        super().__init__(initial_ammount, account_name)
        self.fee = 5000

    def withdraw(self, amount):
        try:
            self.viable_transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print('\nWithdraw Complete.')
            self.get_balance()
        except balance_exception as error:
            print('\nWithdraw Interrupted: {error}')
