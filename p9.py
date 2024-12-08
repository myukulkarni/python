class Fitness:
    def __init__(self,info):
        self.date=info[0]
        self.steps=info[1]
        self.calories=info[2]
        self.active_minutes=info[3]
        self.steps_goal=info[4]
        self.display()

    def display(self):
        print("date:",self.date)
        print("steps:",self.steps)
        print("calories:",self.calories) 
        print("active minutes:",self.active_minutes)   
        print("steps_goal:",self.steps_goal)
        self.check()

    def check(self):
        if self.steps==self.steps_goal:
            print("congratualtions!!,you have done with your goal today..")   
        elif self.steps<self.steps_goal:
            print("yehhhh!!! , come on .. uh hav to complete  ur goal of the day")     
        elif self.steps>self.steps_goal:
            print("wowwww!!!!, uh are beyond your goal..")

F1=Fitness(["12/12/2024",10000,1000,30,1000])        