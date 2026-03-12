tup1=(1,2,3,("Python","Java","C"),"Hello",True)
tup2=(4,5,6,7,8,9,0)
print(f"Tuple1 : {tup1}")
print(f"Tuple2 : {tup2}")
print(f"1st element of {tup1} and {tup2} are {tup1[0] , tup2[0]}")
print(f"Last element of {tup1} and {tup2} are {tup1[-1] , tup2[-1]}")
print(f"Slicing of {tup1} from 0 to last = {tup1[0:]}")
print(f"Slicing of {tup2} from 0 to last = {tup2[0:]}")

print(f"Concatenation of Tuple 1 and 2 is: {tup1 + tup2}")

print("All elements in tup 1 are: ")
for i in tup1:
    print(i)

print(f"Repetition of Tuple1 2 times is: {tup1*2}")