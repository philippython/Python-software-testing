class Account:

    def __init__(self, name: str, acc: str) -> None:
        self.name = name
        self.acc = acc
        self.balance = 0.00
    
    def show_menu(self):
        return 'Welcome back %s , Your Current balance #%s Acount Number : %s' % (self.name, self.balance, self.acc)

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

    def transfer(self, amount: float):
        if self.balance > amount:
            self.balance -= amount
            return 'Withdrawal Successful\nYour Available Balance is #%s' % (self.balance)
        return 'Insufficient Funds\nYour Available Balance is #%s' % (self.balance)

        
        