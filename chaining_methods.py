class User:
    def __init__(self, uName, ballance = 0):
        self.name = uName
        self.ballance = ballance
    
    def deposit(self, amount):
        self.ballance += amount
        return self

    def make_withdrawal(self, amount):
        self.ballance -= amount
        return self
    
    def display_user_balance(self):
        print("User:", self.name, " |  Ballace:", self.ballance)
        return self
    
    def tranfer_money(self, other_user, amount):
        self.ballance -= amount
        other_user.ballance += amount
        return self

fes = User("Fes", 100)
matt = User("Matthew", 690)
marley = User("Marley", 2)

fes.deposit(100).deposit(150).deposit(100).make_withdrawal(425).display_user_balance()
matt.deposit(425).deposit(500).make_withdrawal(1000).make_withdrawal(400).tranfer_money(fes, 25).display_user_balance()
marley.deposit(2).make_withdrawal(1).make_withdrawal(1).make_withdrawal(1).display_user_balance()

fes.display_user_balance()