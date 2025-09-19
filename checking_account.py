from bank_account import BankAccount

class CheckingAccount(BankAccount):
    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number, transfer_limit=500):
        super().__init__(customer_name, current_balance, minimum_balance, account_number, routing_number)
        self._transfer_limit = transfer_limit

    def transfer(self, amount, other_account):
        if amount > self._transfer_limit:
            return f"Transfer failed: exceeds transfer limit of {self._transfer_limit}"
        elif self._current_balance - amount < self._minimum_balance:
            return "Transfer failed: insufficient funds."
        else:
            self._current_balance -= amount
            other_account.deposit(amount)
            return f"Transferred {amount} to {other_account.customer_name}"