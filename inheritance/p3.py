class Employee:
    def __init__(self, info):
        self.name = info[0]
        self.emp_id = info[1]
        
        self.show_details()

    def show_details(self):
        print("Employee Name:", self.name)
        print("Employee ID:", self.emp_id)
        self.payment_status=input("enter payment status(Done/Pending)")

class Manager(Employee):
    def __init__(self, info):
        super().__init__(info)  
        self.check_payment_status()

    def check_payment_status(self):
        if self.payment_status == "done":
            print("Payment Successful")
        else:
            print("Salary Pending")

E1 = Manager(["Mayuri", 1234,])
