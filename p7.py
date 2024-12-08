class Cart:
    def __init__(self,info):
        self.product=info[0]
        self.price=info[1]
        self.quantity=info[2]
        self.calculate()

    def calculate(self):
        self.total= self.price*self.quantity
        self.display()

    def display(self):
        print("product:",self.product)
        print("price:",self.price)
        print("quantity:",self.quantity)
        print("Amount payable",self.total)

C1=Cart(["Sari",500,2])        

    
