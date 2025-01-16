class Bank:
    def __init__(self,account_no,name,type,balance):
        self.account_no=account_no
        self.name=name
        self.type=type
        self.balance=balance
    def deposit(self,amt):
        if amt<=0:
            print("enter the positive number")
        else:
            self.balance+=amt
            print("the balance amount is",self.balance)
    def withdrawal(self,amt):
        if amt<=0:
            print("enter the positive number")
        elif amt>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amt
            print("the balance amount is",self.balance)
    def display(self):
        print(f"Account number :,{self.account_no}")
        print(f"Account Holder Name :, {self.name}")
        print(f"Account type :, {self.type}")
        print(f"Balance Amount :, {self.balance}")
no=int(input("enter the account number :"))
name=input("enter the account holder name : ")
type=input("enter the account type : ")
balance=int(input("enter the balance amount :"))
user1=Bank(no,name,type,balance)
while True:
    print("1)DEPOSIT /n 2)WITHDRAWAL /n 3)DISPLAY /n 4)EXIT")
    opt=int(input("enter an option : "))
    if opt==1:
        amt=int(input("enter an amount :"))
        user1.deposit(amt)
    elif opt==2:
        amt=int(input("enter an amount :"))
        user1.withdrawal(amt)
    elif opt == 3:
        user1.display()
    else:
        print("invalid")


