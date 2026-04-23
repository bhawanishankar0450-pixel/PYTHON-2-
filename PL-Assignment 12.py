#Write a Python program to count the total number of rows in a CSV file.


import csv
from pathlib import Path

#Lets make a read function first

def read(file):
    print("------------------------------------------------")

    print("Reading the csv files")

    with open(file,"r") as csvread:
        csvreader = csv.reader(csvread)
        counter = 0
        for row in csvreader:  
            counter +=1

    print(f"Total number of rows in the given csv file = {counter}")

    print("------------------------------------------------")


#Lets make a file now

filename1 = Path("Students.csv")

if filename1.exists():
    print("File already exists.\nDo you want to Overwrite?\nYes|No")
    option = input(":").lower()

    if option == "no":
        read(filename1)
        quit()


Values = [["James" , 25 , 12],
          ["Bob" , 24, 12] ] 

with open(filename1, "w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(Values)

read(filename1)

#NOTE --> Clearing a csv file

with open(filename1 , "r+") as f:
    f.truncate(0)   #--> Sets the number of bytes of the csv file to 0, effectively clearing it'''