class Account(object):
    def __init__(self, number, balance):
        self.__number = number  # account number    - string
        self.__balance = balance  # current balance   - integer

    # See Balance
    def get_balance(self):
        return self.__balance

    # Deposit
    def add_balance(self, amount):
        self.__balance += amount
        return self.__balance

    # Withdraw
    def sub_balance(self, amount):
        self.__balance -= amount
        return self.__balance

    # Get Account Number
    def get_number(self):
        return self.__number
