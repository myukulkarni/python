class BankAccount:
    def __init__(self,info):
        self.account_number =info[0]
        self.account_holder =info[1] 
        self.balance =info[2]
        self.amount=info[3]
        self.deposit()

    def deposit(self):
        if self.amount > 0:
            self.balance += self.amount
           
            print("amount diposited successfully",self.amount)
            print("new balance",self.balance)
        else:
            print("Deposit amount must be positive.")
        self.withdraw()    

    def withdraw(self): 
        if self.amount > self.balance:
            print("Insufficient balance. Withdrawal failed.")
        elif self.amount > 0:
            self.balance -= self.amount
            print(self.amount,"withdrawal successful")
            print("new balance",self.balance)
        else:
            print("Withdrawal amount must be positive.")
        self.check_balance()    

    def check_balance(self):
        print("available balance",self.balance)



B1 = BankAccount(["123456789", "mayuri", 500,1000])


