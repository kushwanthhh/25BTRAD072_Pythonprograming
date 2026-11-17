class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance or invalid amount!")

    def check_balance(self):
        print("Current Balance: Rs.", self.balance)

    def display_details(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance: Rs.", self.balance)

# Creating an object
name = input("Enter account holder name: ")
acc_no = input("Enter account number: ")

account = BankAccount(name, acc_no)

while True:
    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.check_balance()

    elif choice == 4:
        account.display_details()

    elif choice == 5:
        print("Thank you for using our bank!")
        break
    else:
        print("Invalid choice! Try again.")
