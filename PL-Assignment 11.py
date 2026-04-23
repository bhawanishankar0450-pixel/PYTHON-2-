#Write a program to demonstrate fundamental file handling operations including opening a file, reading its contents, 
#writing data to it, appending additional content and ensuring proper closing of the file.


#csv

import csv

#Writing and Reading

Fields = ["Name", "Roll_No", "Age"]
values = [["James",1,18],
          ["Bob",2,20] ]

filename = "prac.csv"

with open (filename, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(Fields)
    writer.writerows(values)


readfile = open(filename,"r")

readerfile = readfile.read()

print(readerfile)

readfile.close()


