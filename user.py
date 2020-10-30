class User:
    def __init__(self, uName, ballance = 0):
        self.name = uName
        self.ballance = ballance
    
    def deposit(self, amount):
        self.ballance += amount

    def make_withdrawal(self, amount):
        self.ballance -= amount
        return self
    
    def display_user_balance(self):
        print("Ballace:", self.ballance)
    
    def tranfer_money(self, other_user, amount):
        self.ballance -= amount
        other_user.ballance += amount

fes = User("Fes", 100)
matt = User("Matthew", 690)
marley = User("Marley", 2)

fes.deposit(100)
fes.deposit(150)
fes.deposit(100)
fes.make_withdrawal(425)

matt.deposit(425)
matt.deposit(500)
matt.make_withdrawal(1000)
matt.make_withdrawal(400)
marley.deposit(2)
marley.make_withdrawal(1)
marley.make_withdrawal(1)
marley.make_withdrawal(1)

matt.tranfer_money(fes, 25)

fes.display_user_balance()
matt.display_user_balance()
marley.display_user_balance()