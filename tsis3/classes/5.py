class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}tg. New balance: {self.balance}tg")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Withdrawal failed. Available balance: {self.balance}tg")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}tg. New balance: {self.balance}tg")
            
a = BankAccount("Zhanibek", 0)

a.deposit(1000)

a.withdraw(999)

