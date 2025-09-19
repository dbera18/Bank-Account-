from savings_account import SavingsAccount
from checking_account import CheckingAccount

def main():

    # Create Savings accounts
    s1 = SavingsAccount("JD Patel", 2000, 100, "SAV001", "RT001", 0.05)
    s2 = SavingsAccount("Dev Bera", 1500, 100, "SAV002", "RT002", 0.03)

    # Create Checking accounts
    c1 = CheckingAccount("Dev Patel", 3000, 200, "CHK001", "RT003", 400)
    c2 = CheckingAccount("Raki", 1200, 150, "CHK002", "RT004", 300)

    print("\n-- Scenario 1: Savings -")
    print(s1.deposit(500))
    print(s1.apply_interest())

    print("\nScenario 2: Checking --")
    print(c1.withdraw(600))
    print(c1.transfer(350, s2))   # valid
    print(c1.transfer(600, s1))   # exceeds limit

    print("\nFinal Info ")
    s1.print_customer_information()
    s2.print_customer_information()
    c1.print_customer_information()
    c2.print_customer_information()

if __name__ == "__main__":
    main()
