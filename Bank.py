class BankAccount:
    def __init__(self,acc_no,bal):
        self.acc_no=acc_no
        self.balance=bal

    def deposit(self):
        amt=float(input("Enter amount to deposit: "))
        self.balance+=amt
        print(f"Total balance: {self.balance}")

    def withdraw(self):
        amt=float(input("Enter amount to withdraw: "))
        if amt<=self.balance:
            self.balance-=amt
            print(f"Total: {self.balance}")

        else:
            print("Not enough money")

    def check(self):
        print(f"Total balance: {self.balance}")


acc_no=int(input("Enter your account number: "))
bal=float(input("Enter your initial balance: "))
obj=BankAccount(acc_no,bal)
print("\nWelcome")

while True:
    
    print("\n1:Deposit")
    print("2:Withdraw")
    print("3:Check Balance")
    print("4:Exit")

    option=int(input("Enter an option: "))

    if option==1:
        obj.deposit()

    elif option==2:
        obj.withdraw()

    elif option==3:
        obj.check()

    elif option==4:
        print("Exit")
        break

    else:
        print("Invalid option")
