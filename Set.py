set1={0,1,2,3,4}
set2={5,6,7,8,9}
print(f"""
Set1: {set1} 
Set2: {set2}""")

union=set1|set2
print(f"Union of these sets is: {union}")

intersection=set1&set2
print(f"And intersection is: {intersection}")

diff=set1-set2
print(f"And difference is: {diff}")