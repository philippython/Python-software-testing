class Account:

    def __init__(self, name: str, account_num: int) -> None:
        self.name = name
        self.account_num = account_num
        self.balance = 0.00
    
    def show_menu(self):
        return 'Welcome back %s , Your Current balance #%s Acount Number : %s' % (self.name, self.balance, self.account_num)

    def get_balance(self):
        return 'Your Available Balance is #%s' % (self.balance)

    def deposit(self, amount: float):
        self.balance += amount
        return 'Deposit Successful\nYour Available Balance is #%s' % (self.balance)

    def withdraw(self, amount: float):
        if self.balance > amount:
            self.balance -= amount
            return 'Withdrawal Successful\nYour Available Balance is #%s' % (self.balance)
        return 'Insufficient Funds\nYour Available Balance is #%s' % (self.balance)

    def transfer(self, account, amount: float):
        if self.balance > amount:
            self.balance -= amount
            account.balance += amount
            return 'Transfer Successfully made to %s \nYour Available Balance is #%s' % (account.name, self.balance)
        return 'Insufficient Funds\nYour Available Balance is #%s' % (self.balance)


# creating account object

wunmi = Account('wunmi', 2395495344)

# using the show_menu method

print(wunmi.show_menu())

# using the get balance method 

print(wunmi.get_balance())

# using the deposit method

print(wunmi.deposit(56000.87))

#  using the withdrawal method

print(wunmi.withdraw(16790.87))

#  Attempting overdraft 

print(wunmi.withdraw(59403.87))

#  using the transfer method

# The transfer method takes another account object as a parameter
# Creating a new account object 

john = Account('john', 4446748863)

#  using the transfer method

print(wunmi.transfer(john, 20000.00))

# checking wunmi's balance after making transfer

print(wunmi.get_balance())

#  checking john's balance after receiving transfer 

print(john.get_balance())