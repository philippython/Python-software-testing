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


#   

    