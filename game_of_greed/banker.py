
class Banker:
    def __init__(self):
        self.balance = 0
        self.shelved = 0
    
    def shelf(self, val):
        self.shelved += val

    def bank(self):
        self.balance += self.shelved
        self.shelved = 0
    def clear_shelf(self):
        self.shelved = 0


"""

shielved    balance
0             0
0 + 100       0
0           0 + 100
50           100
0            100

"""


      