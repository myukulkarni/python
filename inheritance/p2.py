class HR:
    def __init__(self, info):
        self.project = info[0]
        self.dead_line = info[1]

class team1(HR):
    def __init__(self, info):
        super().__init__(info)
        self.status = input("Enter status of the project (team1): ")
        if self.status == "done":
            print("Frontend is done by team1")

class team2(HR):
    def __init__(self, info):
        super().__init__(info)
        self.status2 = input("Enter status of the project (team2): ")
        if self.status2 == "done":
            print("Backend is done by team2")

class ceo(team1, team2):
    def __init__(self, info):
        super().__init__(info)

        if self.status == "done" and self.status2== "done":
            print("Project successful")


p1 = ceo(["Algosys", "15/12/2024"])
