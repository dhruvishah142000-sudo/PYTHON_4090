'''6. Banking System Using Functions

Functions for:
o Deposit
o Withdraw
o Check Balance'''

print("1. Deposit..")
print("2. Withdraw..")
print("3. Check Balance..")

ch = int(input("Enter Choice : "))
balance = 20000

if ch==1:
    amount = float(input("Enter Amount : "))
    def deposit(amt,bal):
        bal += amt
        print(f"\n Total Balance is : {bal}")
    deposit(amount,balance)

elif ch==2:
    amo = float(input("Enter Amount : "))
    def withdraw(amt,bal):
        balance -= amt
        print(f"\n Total Balance after withdraw: {balance}")
    withdraw(amo,balance)

else:
    def check_bal(balance):
        print(f"\n Total Balance is : {balance}")
    check_bal(balance)
