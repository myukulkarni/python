class student :
    def __init__(self,name,std,ssc_marks,hsc_marks,first_year_marks):
        self.name=name
        self.std=std
        self.ssc_marks=ssc_marks
        self.hsc_marks=hsc_marks
        self.first_year_marks=first_year_marks

    def display(self):
        print('Name = ',self.name)  
        print('class= ',self.std)
        print('10th marks= ',self.ssc_marks)
        print('12th marks= ',self.hsc_marks)
        print('1s year marks= ',self.first_year_marks)

s1=student('mayuri','2nd year','87%','87%','9.60sgpa')     
s1.display()   

         
        


    
