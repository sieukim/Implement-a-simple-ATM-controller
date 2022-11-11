class Card(object):
    def __init__(self, number, password, accounts):
        self.__number = number  # card number       - string
        self.__password = password  # card password     - string
        self.__accounts = {account.get_number(): account for account in
                           accounts}  # linked accounts   - dictionary (key-account_number/value-account_object)

    # Check PIN
    def check_password(self, password):
        return self.__password == password

    # Get Card Number
    def get_number(self):
        return self.__number

    # Get Account dictionary
    def get_accounts(self):
        return self.__accounts
