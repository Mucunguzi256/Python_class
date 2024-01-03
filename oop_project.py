from bank_accounts import *

Mucu = BankAccount(1000000, 'Mucu')
Zolla = BankAccount(2000000, 'Zolla')
Mucu.get_balance()
Zolla.get_balance()

Zolla.deposit(500000)
Mucu.withdraw(200000)
Zolla.withdraw(3000000)
Zolla.withdraw(300000)
Mucu.transfer(900000, Zolla)
Mucu.transfer(50000, Zolla)

Jim = Interest_rewards_account(1000000, 'Jim')
Jim.get_balance()
Jim.deposit(100000)
Jim.transfer(100000, Mucu)

Blaze = Savings_account(1000000, 'Blaze')
Blaze.get_balance()
Blaze.deposit(100000)
Blaze.transfer(1000000, Zolla)
