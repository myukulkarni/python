class Library:
    
    def __init__(self,info):
      
        self.title=info[0]
        self.author=info[1]
        self.ISBN=info[2]
        self.issue_date=info[3]
        self.return_date=info[4]
        self.display()

    def display(self):
        print("Book name:",self.title)    
        print("Author:",self.author)
        print("ISBN no.:",self.ISBN)
        print("issued on:",self.issue_date)
        print("return on:",self.return_date)

  
L1=Library(["Shyamachi aai","sane guruji",123456,"12/12/2024","20/12/2024"])   
