"""
Created on Nov 21, 2015

@author: francisparan
"""


class BankAccount(object):
    def __init__(self, balance = 0):
        print "Initializing balance"
        
        self.balance = balance
    
    @property
    def balance(self):
        print "Getting balance"
        
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Can't set balance to negative")
        
        print "Setting balance"
        self._balance = value

if __name__ == '__main__':
    
    acct = Bank_Account(100)
    
#     Will raise ValueError for negative values
#     acct = Bank_Account(-100)
#     acct.balance = -50
    
    print acct.balance
    
    acct.balance += 50
    
    print acct.balance
    