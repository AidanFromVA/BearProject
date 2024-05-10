import unittest
from atm_controller import ATMController
from bank_api import BankAPI

class TestATMController(unittest.TestCase):
    def setUp(self):
        self.bank_api = BankAPI()
        self.atm = ATMController(self.bank_api)
        self.atm.insert_card("123456789")

    def test_pin_validation(self):
        self.assertTrue(self.atm.enter_pin("1234"))
        self.assertFalse(self.atm.enter_pin("0000"))

    def test_account_selection(self):
        self.atm.enter_pin("1234")
        self.assertTrue(self.atm.select_account("Checking"))
        self.assertFalse(self.atm.select_account("Nonexistent"))

    def test_transactions(self):
        self.atm.enter_pin("1234")
        self.atm.select_account("Checking")
        self.assertEqual(self.atm.check_balance(), 500)
        self.assertTrue(self.atm.deposit(100))
        self.assertEqual(self.atm.check_balance(), 600)
        self.assertTrue(self.atm.withdraw(100))
        self.assertEqual(self.atm.check_balance(), 500)

if __name__ == "__main__":
    unittest.main()
