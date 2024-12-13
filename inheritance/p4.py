class Library:
    def __init__(self, info):
        self.title = info[0]
        self.author = info[1]
        self.isbn = info[2]
        self.display()

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("ISBN:", self.isbn)


class Issue(Library):
    def __init__(self, info):
        super().__init__(info)
        self.issue_date = input("Enter issue date: ")
        self.return_date = input("Enter return date: ")
        self.returned_date = input("Enter returned date: ")
        self.check_return()

    def check_return(self):
        if self.return_date == self.returned_date:
            print("Returned on time")
        else:
            print("Delayed return. Pay penalty of 50 rupees.")



A1 = Issue(["Hackbreakers", "Disha H", "1"])
