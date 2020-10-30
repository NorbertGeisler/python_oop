
class User:
    def __init__(self, uName, ballance = 0):
        self.name = uName
        self.account = Bank_Account(int_rate = 0.01, ballance = 0)
    
    def deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_account_info(self):
        self.account.display_account_info()
        return self
    
class   Bank_Account:
    def __init__(self, int_rate = 0.01, ballance = 0):
        self.int_rate = int_rate
        self.ballance = ballance

    def deposit(self, amount):
        self.ballance += amount
        return self

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.account_balance -= 5
        return self
    
    def display_account_info(self):
        print("Ballance:", self.ballance)
        return self

    def yield_interest(self):
        if self.ballance > 0:
            self.ballance += self.int_rate * self.ballance
        return self

fes = User("Fes")
fes.deposit(100).display_account_info()