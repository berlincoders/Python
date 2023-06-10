#write a program dat the price of a product charge in euros with two decimals

#####  metodo para convertir una string in to a list


#5,85E  we wantwed to have 5 un 85 cent

#price=input("Insert the price in Euros")

#price_split=price.split(",")  # es la lista



#print(int_price)   # para poder la lista

#print(f" El precio en euros {price_split[0]}    y los centimos {price_split[1]}")



#Variante 2
preis="500.99"
punnk=preis.find(".")
print(punnk)   # imprime en que posicon esta el punto
euro= preis[0:punnk]
print(euro)
cents=preis[punnk+1:]
print(cents)

print(f" {euro} euro und {cents} Cent")




