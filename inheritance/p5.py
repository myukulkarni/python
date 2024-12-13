class KandaPoha:
    def __init__(self, info):
        self.name = info[0]
        self.cast = info[1]
        self.display()

    def display(self):
        print("Name:", self.name)
        print("Cast:", self.cast)


class Check(KandaPoha):
    def __init__(self, info):
        super().__init__(info)  
        self.behaviour = input("Enter behaviour (good/bad): ")
        self.looks = input("Enter about looks (good/bad): ")
        self.education = input("Enter education (graduate/not graduate): ")
        self.check_criteria()

    def check_criteria(self):
        if self.behaviour == "good" and self.looks == "good" and self.education == "graduate":
            print("Girl accepted")
        else:
            print("Not accepted")


G1 = Check(["Chingi", "Hindu"])
