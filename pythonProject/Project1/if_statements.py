# the sentence if must be at the begining of the line
#If Anweisung


#if (True):
#  print ("es is wahr") # muy importante la tabulacion

########## Alles comentieren

#if (100>80 and "abcde"<"z"):
#    print("es ist wahr")

#if ((100>80 and "abcde"<"z")  and 4==4*2):
#   print("es ist wahr")
#
# else:
#    print(" das da oben ist falsch")

#angabe= "8"
#if (type(angabe)==int):
#    print("integer")
#elif (type(angabe)==bool):
#    print("boolean")
#elif (type(angabe)==str):
#    print("string")
#elif (type(angabe)==float):
#    print("float")
#else:
# print("Datetyp unbekannt")
# Diferencias entre if y ifelse


#####################################

gehalt= 5000

if(gehalt>=2000):
    print("Gut  Verdiener")
    if(gehalt>5000):
       print("Top Verdiener")
    else:
        print("gehalt zwisen 200 un 5000 oder gleich  5000")
else:
    print("Gehalt kleiner 2000")














is_male = False
is_tall = False
if is_male and is_tall:
     print(" you are a tall male ")
elif is_male and not(is_tall):
    print(" you are a short male")
elif not(is_male) and is_tall:
    print(" you are not a  male but are tall")
else:
     print(" you are not a male and not tall")

def max_num (num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num( 3,400,5))



