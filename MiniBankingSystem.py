class CheckPin:
    def verify(self, pin):
        return pin in [1111, 2222, 3333]

class Balance:
    def __init__(self):
        self.bal = 2000

    def get_balance(self):
        return self.bal

    def update_balance(self, amount):
        self.bal += amount

class Transaction:
    def __init__(self, balance):
        self.balance = balance

    def process(self, amt):
        pass

class Withdraw(Transaction):
    def process(self, amt):
        if amt <= self.balance.get_balance():
            self.balance.update_balance(-amt)
            print(f"Amount Withdrawn: {amt}")
            print(f"Remaining Balance: {self.balance.get_balance()}")
            print("Transaction Successful")
        else:
            print("Insufficient Balance")

class Deposit(Transaction):
    def process(self, amt):
        self.balance.update_balance(amt)
        print(f"Amount Deposited: {amt}")
        print(f"New Balance: {self.balance.get_balance()}")

class ATM:
    def __init__(self):
        self.balance = Balance()
        self.count = 0

    def run(self):
        while True:
            pin = int(input("Enter Pin Number: "))
            if 1000 <= pin <= 9999:
                cpn = CheckPin()
                if cpn.verify(pin):
                    print("Enter Your Choice")
                    print("1. Withdraw  2. Deposit")
                    ch = int(input())
                    amt = int(input("Enter Amount: "))
                    if amt > 0 and amt % 100 == 0:
                        if ch == 1:
                            wd = Withdraw(self.balance)
                            wd.process(amt)
                        elif ch == 2:
                            dp = Deposit(self.balance)
                            dp.process(amt)
                        else:
                            print("Invalid Choice")
                        break
                    else:
                        print("Invalid Amount")
                else:
                    print("Invalid Pin")
                    self.count += 1
            else:
                print("Incorrect Pin")
                self.count += 1

            if self.count == 3:
                print("Blocked")
                break

# Running the ATM
atm = ATM()
atm.run()
