import random

#Generate a random valuem from 1 to 49
#‚value=random.randint(1,49)
#Generate the supermumber from 0 to 9
superzahl=random.randint(0,9)

i=0
bet=[]
while i<= 5:
     # print(value), not necesary to print the value
     value = random.randint(1, 49)
     # Add the value to the array
     bet.append(value)
     # incrase the counter
     i=i+1
     if i==6 :
          print(bet)
print("Done with the bet")
print("Superzahl is " ,superzahl )













