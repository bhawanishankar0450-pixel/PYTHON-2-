d = {"name": "Amit", "age": 18, "city": "Pune"}

print("Dictionary:", d)
print("Name:", d["name"])

d["age"] = 19
d["course"] = "Python"
print("After Update:", d)

d.pop("city")
print("After Removing Element:", d)

d2 = {"marks": 90, "grade": "A"}
d.update(d2)

print("After Merging Dictionaries:", d)