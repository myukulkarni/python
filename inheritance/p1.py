class HOD:
    print("Register for HOD's program")
    password_counter = 1000  
    password_list = []

    def __init__(self, info):
        self.name = info[0]
        self.Dept = info[1]
        self.register()

    def register(self):
        
        self.email_id = input("Enter email id: ")
        self.phone_no = int(input("Enter phone no.: "))
        self.DOB = input("Enter your date of birth: ")
        self.dept = input("Enter your department: ")
        self.generate_password()

    def generate_password(self):
        while True:
            if HOD.password_counter not in HOD.password_list:
                self.password = HOD.password_counter
                HOD.password_list.append(self.password)
                HOD.password_counter += 1
                break
        print("Password:", self.password)
        print("Registration successful!")
        print("Please log in with your email and generated password.")
        self.login()

    def login(self):
        self.loginemail = input("Enter your email: ")      
        self.loginpassword = input("Enter your password: ")

        if self.loginemail == self.email_id and self.loginpassword == str(self.password):
            print("Login successful!")
            print("Welcome to the program!!")
        else:
            print("Invalid credentials")

class Professor(HOD):
    def __init__(self, info):
        super().__init__(info)
    print("Register for professor's program")
    
        
        

class Student(HOD):
    def __init__(self, info):
        super().__init__(info)
    print("Register for student program")    

HOD1 = HOD(["Mayuri", "CSE"])
Professor1 = Professor(["Manoj", "CSE"])
Student1 = Student(["Madhura", "CSE"])
