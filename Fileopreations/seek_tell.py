#Seek to move the pointer and Tell to tell the current pointer position

f=open("K.txt", "a+")
print("first file pointer position", f.tell())

f.write(" python")
print("After write file pointer position", f. tell())

f.seek(0)
print("After file pointer position change", f. tell())

print(f.read())

f.close()
