'''
Created on Sep 19, 2015

@author: francisparan
'''

class LogIn():
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, val):
        self.__password = val    
    
samp = LogIn('fdp90', 'sap')
print samp.password