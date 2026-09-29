# Read a CSV File
#csv is a comma seperated value and stores in row and columns 
import csv

f=open("data.csv","r")

r=csv.reader(f)

for i in r:
    print(i)

f.close()
