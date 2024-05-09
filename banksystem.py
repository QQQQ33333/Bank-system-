'''Write a python program to replicate a Banking system. The following features are mandatory:
1. Account login
2. Amount Depositing
3. Amount Withdrawal
Other than the above features you can add any other also.
'''
from datetime import *
class BANKSYSTEM:

    def __init__(self,name,accountNo,username):
        self.name=name
        self.accountNo=accountNo
        self.username=username
        self.balance=0
    def confidential(self,password):
        self.password=password
    def transaction(self):
        if "mybank@123" ==self.password:
            print('login successfully')
            d = datetime.now()
            print('account no:', self.accountNo)
            print('your name:', self.name, '\nyour balance:', self.balance, '\n date:', str(d))
        else:
            print("INCORRECT PASSWORD,RETRY or CHOOSE EXIT")
    def deposit(self):
        self.amount = float(input('enter amount to be deposited:Rupees '))
        self.balance += self.amount
        d = datetime.now()
        print('amount deposited:Rupees',self.balance,'\ntransaction date:', str(d))
    def withdraw(self):
        if 'mybank@123' == self.password:
            print('login successfully')
            self.amount = float(input('enter amount to be debited:Rupees '))
            if self.balance >= self.amount:
                self.balance -= self.amount
                d = datetime.now()
                print('Rupees', self.amount, 'is debited from your account')
                print('your balance: rupees ', self.balance, '\ntransaction date:', str(d))
            else:
                print('sorry,your account balance is insufficient')
        else:
            print("INCORRECT PASSWORD,RETRY or CHOOSE EXIT")
B=BANKSYSTEM(input('name:'),input('accountNo:'),input('username:'))
def choice():
    print("Select an option")
    print("0.Transaction\n1.Deposit\n2.Withdraw\n3.Exit")
r1 = choice()
print(r1)
o = int(input("Enter Your Option:"))
while True:
    if o == 0:
        B.confidential(input('password:'))
        B.transaction()
        r0 = choice()
        print(r0)
        o = int(input("Enter Your Option:"))

    elif o == 1:
        B.deposit()
        r2 = choice()
        print(r2)
        o = int(input("Enter Your Option:"))

    elif o == 2:
        B.confidential(input('password:'))
        B.withdraw()
        r3 = choice()
        print(r3)
        o = int(input("Enter Your Option:"))

    elif o == 3:
        print("Thank you,you are exited from the home page.\nvisit again")
        break
    else:
        print('you entered an invalid choice.RETRY')
        r1 = choice()
        print(r1)
        o = int(input("Enter Your Option:"))
else:
    print('RETRY AFTER 1Hr')





