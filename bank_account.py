class BankAccount:
    bank_title = "D&D Bank"   # shared by all accounts

    def __init__(self, customer_name, current_balance, minimum_balance, account_number, routing_number):
        self.customer_name = customer_name
        self._current_balance = float(current_balance)   # protected
        self._minimum_balance = float(minimum_balance)   # protected
        self.__account_number = account_number           # private
        self._routing_number = routing_number            # protected

    def deposit(self, amount):
        self._current_balance += amount
        return f"{amount} is deposited. Current Balance: {self._current_balance}"

    def withdraw(self, amount):
        remaining_balance = self._current_balance - amount
        if remaining_balance >= self._minimum_balance:
            self._current_balance -= amount
            return f"{amount} withdrawn. Current Balance: {self._current_balance}"
        else:
            return f"Cannot Withdraw {amount}! Minimum balance must be: {self._minimum_balance}"

    def print_customer_information(self):
        print(f"\n--- {self.bank_title} ---")
        print(f"Customer Name: {self.customer_name}")
        print(f"Account Number: {self.__account_number}")
        print(f"Routing Number: {self._routing_number}")
        print(f"Current Balance: {self._current_balance}")
        print(f"Minimum Balance: {self._minimum_balance}")