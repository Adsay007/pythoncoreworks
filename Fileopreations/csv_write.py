# Write a CSV file 
import csv

f=open("data.csv","w",newline="")

content= [
    ['name','age','place'],
    ['arun',25,'ekm'],
    ['amal',26,'tvm']
]

w=csv.writer(f) # creates a writer object
w.writerows(content) # writes each row into the file 
f.close()