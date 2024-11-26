# try:
#     # Trying to open a file that doesn't exist
#     file = open('emptyfile.txt', 'r')
#     content = file.read()
#     print(content)

# except FileNotFoundError:
#     # Catching the FileNotFoundError if the file is not found
#     print("Error: The file you are trying to open does not exist.")

# finally:
#     print("File operation completed.")


# try:
#     # Attempting to add a string and an integer, which causes a TypeError
#     result = "Hello" + 5
#     print(result)
# except TypeError:
#     # Catching the TypeError
#     print("Error: You can't add a string and an integer.")
# finally:
#     print("Type checking completed.")




try:
    f=open("C:\Users\HP\OneDrive\Documents\file.txt", "r") 
    content = f.read()
    print(content)  
except EOFError:
    print("EOFError: Unexpected end of file reached.")
except FileNotFoundError:
    print("Error: The specified file was not found.")


