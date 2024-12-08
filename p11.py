class Shop:
    def __init__(self,info):
        self.available_items=info[0]
        self.needed_items=info[1]
        self.total_amount=info[2]
        self.expenditure=info[3]
        self.profitt()
    
    def profitt(self):
        self.profit=self.total_amount-self.expenditure
        if self.profit>self.expenditure:
            print("greate achhivement!!")
        else:
            print("ohooo!!! uh have to work hard...")    
        self.customers()

    def customers(self):
        self.storage=self.available_items+self.needed_items
    
        if self.storage>self.available_items:
            print("yehhh!!! storage is available")
        else:
            print("ufff!!!, storage is not avaible ")    
        self.sell()

    def sell(self):
        self.selll=self.needed_items
        self.display()
       
    def display(self):
        print("total vailable items:",self.available_items)  
        print("total needed items:",self.needed_items) 
        print("total amount earned",self.total_amount)
        print("total expenditure:",self.expenditure)
        print("total profit generated:",self.profit)
        print("total sell:",self.selll)
        print("total storage :",self.storage)

s1=Shop([500,500,100000,5000])