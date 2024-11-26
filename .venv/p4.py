def search_list(lst, search_term):
    
    search_term = search_term.lower()
    for i in range(len(lst)):
        if lst[i].lower() == search_term:
            return i  
    return -1  


user_list = input("Enter the list items separated by spaces: ").split()


search_term = input("Enter the search term: ")


result = search_list(user_list, search_term)
print("Index:", result)
