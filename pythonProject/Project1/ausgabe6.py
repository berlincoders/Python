
#Un eine bestimmte steuer zu zahlen mussen sie
#uber 16 alt  sein un d ein einkommen von mehr als 100e monat haben
# schiibne sie en program das den benutzer nach seien alter un mONATSINKOMEN FRAGT ES SOLL ANGEZEIR WERDEN OR DER BENUTZES STEUER ZA
#muss oder nighct


#age=int(input(" Please insert your age:"))
#income=int(input("Please provide your monthly income in €:"))

#if  ( age>16  and income>1000):
#    print(" you must to paid taxes")
#else:
#    print("you do not need to paid taxes")

##valiente 2
age=int(input(" Please insert your age:"))
if age>16:
    income = int(input("Please provide your monthly income in €:"))
    if income>1000:
        print("Steuer zahen")
    else:
        print("Steuer frei")
else:
    print("Steuer frei")




