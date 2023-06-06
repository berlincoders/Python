#num1= input("write a number: ")
#num2= input("write a second number: ")
#result=float(num1)+ float(num2)
#print(result)


grosse=1.7
gewicht=70


# by default it is an strig ,
# la solucion mas elegante
#grosse=float(input("grosse in m eingeben: "))
grosse=input("Grosse in M Eigeben:")
gewicht=input("Gewicht in Kg eingeben: ")

f_grosse=float(grosse)
f_gewicht= float(gewicht)


# otra solucion sobreecribir el valor de grosse 
#grosse=float(grosse)

bmi=f_gewicht/f_grosse**2
bmi=round(bmi, 1)
print(bmi)
