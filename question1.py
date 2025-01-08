'''
question1.py


Fix all the errors so that tests in test_question1.py pass and the code
runs as described in the comments and docstring.


TOTAL POINTS AVAILABLE: 10 

Code Functionality (10)
10 points - no errors remain and code runs
-2 points for each remaining error or new ones introduced
0 points - all original errors remain 
'''

class BankAccount:
    '''
    Class to represent a bank account and money being deposited and withdrawn.
    '''
    account_type = 'current'
    business_account = False

    def __init__(self, account_holder, balance=0):
        '''
        Creates the initial account requiring the name of the account holder,
        and with a default starting balance of 0.
        '''
        # set account holder name and balance
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        '''
        Adds money to the account. Deposited amount must be a positive value.
        '''
        # Check if amount being paid in is negative
        if amount < 0:
            # raise ValueError if negative
            raise ValueError('Deposits must be positive values.')

        # add deposit to balance
        self.balance += amount

    def withdraw(self, amount):
        '''
        Withdraws money from the account only if the account has sufficient funds and 
        the amount being withdrawn is a positive number.
        '''
        # check if amount being withdrawn is negative
        if amount < 0:
            # raise ValueError if negative
            raise ValueError('Withdrawals must be positive values')
        # check if sufficient funds are in the account
        if self.balance < amount:
            # raise ValueError if not enough funds
            raise ValueError('Insufficient funds for withdrawal')

        # decrease the balance by the withdrawal amount
        self.balance -= amount

    def get_balance(self):
        '''
        Return the current balance.
        '''
        return self.balance

    def __str__(self):
        '''
        Return a string representation of the bank account.
        '''
        # return a formatted string containing the account holder name and balance
        return f"Account Holder: {self.account_holder}, Balance: £{self.balance:.2f}"
