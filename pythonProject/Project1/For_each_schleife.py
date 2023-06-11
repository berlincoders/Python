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



li=[1,2,3,4,5,6,7]
print(li)
for element in li:
     print(element)

for element in li:
     print(element)
     print("rechnne")
     print(element*100)
     print()
print("Schleife Ende")


teilnemher_liste=["Anton","Berta","Carl"]
gesuchte="Max"   # try with Max

for teilnemer in teilnemher_liste:

   # print(teilnemer)

    if teilnemer == gesuchte:
        print("Gefunden")

    else:
        print(f"{gesuchte} ist nicht dabei")
        teilnemher_liste.append(gesuchte)
        break
print(teilnemher_liste)










