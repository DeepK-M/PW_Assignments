# Base class for Bank Accounts
class BankAccount:
    def __init__(self, account_number, holder_name, balance=0.0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into {self.holder_name}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.holder_name}'s account.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance

    def display_info(self):
        print(f"Account Number: {self.account_number}, Holder: {self.holder_name}, Balance: {self.balance}")


# Subclass for Savings Account
class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0.0, interest_rate=0.03):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added to {self.holder_name}'s Savings Account.")


# Subclass for Checking Account
class CheckingAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance=0.0, overdraft_limit=500):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.holder_name}'s Checking Account.")
        else:
            print("Withdrawal denied! Overdraft limit exceeded.")


# ----------- Testing the Banking System -----------

# Create accounts
savings = SavingsAccount("S123", "Anu", 1000)
checking = CheckingAccount("C456", "Basha", 500)

# Display initial info
savings.display_info()
checking.display_info()

# Deposit money
savings.deposit(500)
checking.deposit(300)

# Withdraw money
savings.withdraw(200)
checking.withdraw(900)  # within overdraft limit

# Add interest to savings
savings.add_interest()

# Balance inquiry
print("Anu's Balance:", savings.get_balance())
print("Basha's Balance:", checking.get_balance())

# Final info
savings.display_info()
checking.display_info()



#Sample Output:
# Account Number: S123, Holder: Anu, Balance: 1000
# Account Number: C456, Holder: Basha, Balance: 500
# Deposited 500 into Anu's account.
# Deposited 300 into Basha's account.
# Withdrew 200 from Anu's account.
# Withdrew 900 from Basha's Checking Account.
# Interest of 39.0 added to Anu's Savings Account.
# Anu's Balance: 1339.0
# Basha's Balance: -100
# Account Number: S123, Holder: Anu, Balance: 1339.0
# Account Number: C456, Holder: Basha, Balance: -100