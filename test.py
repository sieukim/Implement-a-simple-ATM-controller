from src.account import Account
from src.atm import ATM
from src.card import Card
from src.exception import InvalidCardNumberException, InvalidPasswordException, InvalidAccountNumberException, \
    InvalidBalanceException, InvalidTransactionException


###### Test Code
def test():
    # Account Data
    account1 = Account('11-11-11-11', 1000)
    account2 = Account('22-22-22-22', 2000)
    account3 = Account('33-33-33-33', 3000)
    account4 = Account('44-44-44-44', 4000)

    # Card Data
    card1 = Card('1111-1111', '1111', [account1, account2])
    card2 = Card('2222-2222', '2222', [account1, account3])
    card3 = Card('3333-3333', '3333', [account1, account4])
    card4 = Card('4444-4444', '4444', [account1, account2, account3, account4])

    # Create ATM Object
    atm = ATM([card1, card2, card3, card4])

    # Insert Card
    try:
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        atm.insert_card()
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # Check PIN
        atm.check_password()
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # Select Account
        atm.select_account()
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        # See Balance/Deposit/Withdraw
        atm.select_transaction()
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    except InvalidCardNumberException:
        return
    except InvalidPasswordException:
        return
    except InvalidAccountNumberException:
        return
    except InvalidTransactionException:
        return
    except InvalidBalanceException:
        return


test()