# a=int(input("a="))
# b=int(input("b="))
# if a>b:
#     print(True)
# else:
#     print(False)

# name=input("enter a name")
# print(len(name))

# name=input("enter a string: ")
# l=input("enter a letter to find: ")
# print(name.find(l))

# movies=list(map(str,input("enter your 3 fav movies: ").split()))
# print(movies)

# actors=[["srk",[ "movie1","movie2","movie3"]],["shahid",["movie1","movie2",]]]
# print(actors[1][1])



# books=[]
# for i in range(2):
#     temp=["",[]]
#     temp[0]=(input("book_id: "))
    
#     temp[1].append(input("bn: "))
#     temp[1].append(input("an: "))
#     temp[1].append(int(input("r: ")))
#     temp[1].append(int(input("p: ")))
#     books.append(temp)

# # for i in range(len(books)):
# #      print("book_id: ",books[i][0])
# #      print("book_name: ",books[i][1])  
# #   
# print("book details are:")
# for i in range (len(books)):
#     print("details of",i,"book are")
#     print("book_id: ",books[i][0])
#     print("book_name: ",books[i][1][0])
#     print("auther_name: ",books[i][1][1])
#     print("ratings: ",books[i][1][2])
#     print("print: ",books[i][1][3])

# for i in range(len(books)):
#     if books[i][1][2]>130:


class borrow:
    def __init__(self,) :
        pass        
            

class books:
    def __init__(self,id,title,author,publish_date,ratings,price):
        self.id=id
        self.title=title
        self.author=author
        self.publish_date=publish_date
        self.ratings=ratings
        self.price=price
    
    def view_books(self):
        print("book_id: ",self.id)
        print("book_name: ",self.title)
        print("book_author: ",self.author)
        print("publish_date: ",self.publish_date)
        print("ratings: ",self.ratings)
        print("price: ",self.price)         
         
b1=books(1,"the inferno","den","1990",3,150)
b1.view_books()



