import os

def file_read():
    filename = input("Enter the filename: ")
    f = open(filename, "r")
    content = f.read()
    print("--- File Content ---")
    print(content)
    f.close()

def file_write():
    filename = input("Enter the filename: ")
    f = open(filename, "w")
    content = input("Enter the content: ")
    f.write(content)
    f.close()

def file_append():
    filename = input("Enter the filename: ")
    f = open(filename, "a")
    content = input("Enter the content to append: ")
    f.write(content + "\n")
    f.close()

def file_search():
    filename = input("Enter the filename: ")
    search_word = input("Enter the word to search: ")
    f = open(filename, "r")
    
    if search_word in f.read():
        print(f"'{search_word}' was found in the file.")
    else:
        print(f"'{search_word}' was not found.")
    f.close()

def file_delete():
    filename = input("Enter the filename: ")
    # os.path.exists checks if the file is actually there before trying to delete it
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted successfully.")
    else:
        print("File does not exist.")

# Main Menu
print("1.File Read")
print("2.File Write")
print("3.File Append")
print("4.File Search")
print("5.File Delete")
print("6.Exit")

ch = int(input("Enter your choice: "))

if ch == 1:
    file_read()
elif ch == 2:
    file_write()
elif ch == 3:
    file_append()
elif ch == 4:
    file_search()
elif ch == 5:
    file_delete()
else:
    exit()