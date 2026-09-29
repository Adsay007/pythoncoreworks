""" 
File Operations
#open() - to open
#close() - to close

#read 
#readlines() - reads as a list
#write
#writelines() - writes as a list

#import os 
#os.delete(filename) - to delte a file

open (filename, accessmode)

File Accessmode
I.r -read only
2.w-write only
3.a-append
4.rt readtwrite
5.wt
6.at -appendtread

Non Text file like (images, audio, video)
1.rb
2.wb
3.ab
4.rb+
5.wb+
6.abt

binary modes """

# 1. Write a program to read a text file and display the number of lines in a file
f = open('k.txt', 'r')
lines = f.readlines()
print("Number of lines:", len(lines))
f.close()

# 2. Write a program to display the number of words in a file
f = open('k.txt', 'r')
content = f.read()
words = content.split() # split is used to split the single string into indivisual words 
print("Number of words:", len(words))
f.close()

# 3. Write a program to update the second line in a file
f = open('k.txt', 'r')
lines = f.readlines()
f.close()

if len(lines) >= 2:
    lines[1] = "This is the new second line.\n"

f = open('k.txt', 'w')
f.writelines(lines)
f.close()

# 4. Write a program to display the last 5 lines in a file
f = open('k.txt', 'r')
s = f.readlines()
print(s[-5:])
f.close()

# 5. Write a program to display the first 5 lines in a file
f = open('k.txt', 'r')
s = f.readlines()
print(s[:5])
f.close()

# 6. Program to search a particular word in a file using the 'in' operator directly
search_word = "Python"
f = open('k.txt', 'r')

# Checks if the word exists directly in the read output
if search_word in f.read():
    print("The word was found in the file.")
else:
    print("The word was not found.")
    
f.close()