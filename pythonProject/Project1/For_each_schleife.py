###---For each schleife######


# range function puede tener tres parametros, range (star, stop,step), star und step are opcional,

for i in range(15):
    print(f" {i} widerholung")

#  Python beginnt mit dem Zählen bei 0

print()

for i in range(10,21,2):
    print(f" {i} widerholung")

# iterierbares Objekt       -->Listen, Dictionaries ,Generators

obstkorb=["Apfel","Banane","Erdberre","Melone"]

for obst in obstkorb:
    print(obst)
print("Finally finished")

############## Schleife abbrechen ################, Break , Continue

for i in range(5):
    if i == 3: break   # Oder Continue, springt eine numer , is it is not working
    print(i)

# python strings operations,  w3 schooll.com






