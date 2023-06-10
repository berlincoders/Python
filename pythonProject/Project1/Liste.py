
# cada elemento de la lista tiene un index
obst1="birne"
obst2="Banane"
obst3="Apfel"

obst_liste=[obst1,obst2,obst3, "Reis"]
print(type(obst_liste))
print(obst_liste)

num_list=[1,2,3]
some_list=[True,24,"Halllo",[1,2,3],obst_liste]
print(len(some_list))

###########Methoden ########
####apend

some_list.append(2.14)
# print("nach append:",len(some_list))
# print(some_list)

print(some_list[2])
#print(some_list[8])

test= "VHS"
print(test[2])
# test[2]=x

some_list[2]="Bye"
print(some_list)




# print(some_list+"foo") # geht nicht

#print(some_list+ obst_liste)

print(some_list[2]+" bye")

print(some_list[1]*2)

print(some_list)
print(some_list*3)

#########################


new_list =[11,"2",20]

new_list[1]=int(new_list[1])
print(new_list)

result= new_list[0] +new_list[1] +new_list[2]
print(result)



#######################.pop()

some_list.pop(2)   # the last element () por defecto -1
print(some_list)

#########list to str

#test_list=["1","Hallo"]

#list_to_str="#".join(test_list)
#print(list_to_str)

#print(some_list)
#print(some_list[1])
#print(some_list[1:3])
#print(some_list[1:6:2])   #### anfang ende::springe

##### liste in list

print()
list_in_list =[True,None,["a","b"],("a")]
print(list_in_list)
print(len(list_in_list))
print(type(list_in_list))







meine_liste = ["Apfel","Blauberre",34, 2.72]

mein_element=meine_liste[1]  # Este es el elemento 2 puesto que python empiza a contar desde o

print(mein_element)

meine_liste[1] ="Banane"

print(meine_liste)

###### python list veränder  ##### add element

meine_liste.append("Birne")
print(meine_liste)


