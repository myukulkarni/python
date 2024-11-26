 #single inheritance

class parent:
    print("this is  parent class")

class child (parent):
    print("this is child class inheriting properties from parent class")

  #multilevel inheritance 

class parent:
    print("this is  parent class")

class child (parent):
    print("this is child class inheriting properties from parent class")
  
class child2(child):
    print("this is multilevel inheritance")



