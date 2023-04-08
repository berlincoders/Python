# List it is an Array

friends=["Kevin","Julia","Karen","Jim"]
print(friends[-3])
friends[1]="Mike"
print(friends[2:3])
print(friends[1])

# list  continuation
lucky_numbers =[43,8,15,16,23,42]
friends=["Kevin","Julia","Karen","Jim"]
friends.extend(lucky_numbers)

# Add one element to the Array
friends.append("Cris")
print(friends)
# insert one element to the array
friends.insert(1,"Luis")
print(friends)
# remove an element of the list
friends.remove(42)
print(friends)
lucky_numbers.sort()
print(lucky_numbers)
#copy a list
fiends2 =friends.copy()
print(fiends2)