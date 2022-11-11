from src.exception import InvalidCardNumberException, InvalidPasswordException, InvalidAccountNumberException, \
    InvalidBalanceException, InvalidTransactionException


class ATM(object):
    def __init__(self, cards):
        self.__cards = {card.get_number(): card for card in
                        cards}  # available cards   - dictionary (key-card_number/value-card_object)
        self.__card = None  # inserted card     - Card Object
        self.__account = None  # selected account  - Account Object

    # Check if card number is available
    def __valid_card(self, card_number):
        return card_number in self.__cards

    # Check if account number is available
    def __valid_account(self, account_number):
        return account_number in self.__card.get_accounts()

    # Set Inserted Card
    def __set_card(self, card_number):
        self.__card = self.__cards[card_number]

    # Set Selected Account
    def __set_account(self, account_number):
        self.__account = self.__card.get_accounts()[account_number]

    # Initialize Inserted Card
    def __init_card(self):
        self.__card = None

    # Initialize Selected Account
    def __init_account(self):
        self.__account = None

    # See Balance
    def __see_balance(self):
        balance = self.__account.get_balance()
        print(f'Total Balance: {balance}')

    # Deposit
    def __deposit(self):
        amount = int(input('Enter the amount to deposit.\n'))
        balance = self.__account.add_balance(amount)
        print(f'Total Balance: {balance}')

    # Withdraw
    def __withdraw(self):
        amount = int(input('Enter the amount to withdraw.\n'))

        if amount > self.__account.get_balance():
            print('Insufficient Balance.')
            raise InvalidBalanceException()

        balance = self.__account.sub_balance(amount)
        print(f'Total Balance: {balance}')

    # Insert Card
    def insert_card(self):
        card_number = input('Please insert your card.\n')

        if self.__valid_card(card_number):
            self.__set_card(card_number)
        else:
            print('Invalid Card.')
            raise InvalidCardNumberException()

    # Check PIN
    def check_password(self):
        password = input('Please enter your PIN.\n')

        if not self.__card.check_password(password):
            self.__init_card()
            print('You\'ve entered a wrong PIN.')
            raise InvalidPasswordException()

    # Select Account
    def select_account(self):
        print('Please select an account.')
        accounts = list(self.__card.get_accounts())

        for i, account in enumerate(accounts):
            print(f'{i + 1}> {account}')

        selected = int(input()) - 1

        if selected in range(len(accounts)):
            account_number = accounts[selected]
            self.__set_account(account_number)
        else:
            print('You\'ve selected a wrong account.')
            raise InvalidAccountNumberException()

    # select transaction
    def select_transaction(self):
        print('Please Select a Transaction.')
        print('1> See Balance')
        print('2> Deposit')
        print('3> Withdraw')

        transaction = input()

        if transaction == '1':
            self.__see_balance()
        elif transaction == '2':
            self.__deposit()
        elif transaction == '3':
            self.__withdraw()
        else:
            print('You\'ve selected a wrong transaction.')
            raise InvalidTransactionException()
