from bank_api import BankAPI

class ATMController:
    def __init__(self, bank_api):
        self.bank_api = bank_api
        self.user_authenticated = False
        self.card_number = None
        self.selected_account = None

    def insert_card(self, card_number):
        """Please Start the session with the card number"""
        self.card_number = card_number
        self.user_authenticated = False
        self.selected_account = None

    def enter_pin(self, pin):
        """Please Attempt to authenticate with the given pin"""
        if self.bank_api.validate_pin(self.card_number, pin):
            self.user_authenticated = True
            return True
        return False

    def select_account(self, account_type):
        """Please Select an account to operate"""
        if self.user_authenticated:
            accounts = self.bank_api.get_accounts(self.card_number)
            if account_type in accounts:
                self.selected_account = account_type
                return True
        return False

    def check_balance(self):
        """Please Check the balance of the selected account"""
        if self.user_authenticated and self.selected_account:
            return self.bank_api.get_balance(self.card_number, self.selected_account)
        return None

    def deposit(self, amount):
        """Please Deposit amount into the selected account"""
        if self.user_authenticated and self.selected_account:
            return self.bank_api.deposit(self.card_number, self.selected_account, amount)
        return False

    def withdraw(self, amount):
        """Please Withdraw amount from the selected account"""
        if self.user_authenticated and self.selected_account:
            return self.bank_api.withdraw(self.card_number, self.selected_account, amount)
        return False
