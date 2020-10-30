
class   Bank_Account:
    def __init__(self, int_rate = 0.01, ballance = 0):
        self.int_rate = int_rate
        self.ballance = ballance

    def deposit(self, amount):
        self.ballance += amount
        return self

    def withdraw(self, amount):
        self.ballance -= amount
        return self
    
    def display_account_info(self):
        print("Ballance:", self.ballance)
        return self

    def yield_interest(self):
        if self.ballance > 0:
            self.ballance += self.int_rate * self.ballance
        return self
    
bills = Bank_Account(0.02,100).deposit(100).deposit(200).deposit(100).withdraw(350).yield_interest().display_account_info()
savings = Bank_Account(0.1, 500).deposit(200).withdraw(60).withdraw(15).withdraw(20).withdraw(60).yield_interest().display_account_info()
