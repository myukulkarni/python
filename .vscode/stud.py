class Student:
    pnr_counter = 1000  
    pnr_list = []
    
    def __init__(self, stud):
        self.name = stud[0]
        self.email = stud[1]
        self.SSC_Mark = stud[2]
        self.HSC_Mark = stud[3]
        self.GenPNR()
        
    def GenPNR(self):
        while True:
            if Student.pnr_counter not in Student.pnr_list:
                self.pnr = Student.pnr_counter
                Student.pnr_list.append(self.pnr)
                Student.pnr_counter += 1
                break
        self.assign_department_course()

    def assign_department_course(self):
        """Assign department and course based on SSC and HSC marks"""
        if self.SSC_Mark > 70 and self.HSC_Mark > 70:
            self.department = "Computer Science"
            self.course = "B.Tech"
        else:
            self.department = "Electronics"
            self.course = "B.Tech"
        self.display()

    def display(self):
        print("PNR:", self.pnr)
        print("Name:", self.name)
        print("Email:", self.email)
        print("SSC Marks:", self.SSC_Mark)
        print("HSC Marks:", self.HSC_Mark)
        print("Department Assigned:", self.department)
        print("Course Assigned:", self.course)

s1 = Student(["Mayuri", "myu@gmail.com", 88, 87 ])
s2 = Student(["samarth","sam@gmail.com",90,80])
print("Tracked PNRs:", Student.pnr_list)
