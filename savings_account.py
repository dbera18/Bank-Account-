from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def _init_(self, customer_name, current_balance, minimum_balance, account_number, routing_number, interest_rate=0.02):
        super()._init_(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self._interest_rate = interest_rate

    def apply_interest(self):
        interest = self._current_balance * self._interest_rate
        self._current_balance += interest
        return f"Interest applied: {interest:.2f}. New Balance: {self._current_balance:.2f}"
