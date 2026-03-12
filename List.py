list=[1,2,3,4,5]
print(f"List: {list}")

print(f"1st Value in list is: {list[0]}")
print(f"Last Value in list is: {list[-1]}")
print(f"Slicing from 1 to 4 is: {list[0:-2]}")

list.append(6)
print(list)

list.insert(0,0)
print(list)

list.sort()
print(f"Ascending: {list}")

list.reverse()
print(f"Descending: {list}")

list.remove(4)
print(f"List without 4: {list}")

list.clear()
print(f"Empty List: {list}")