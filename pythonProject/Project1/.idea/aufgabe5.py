
# write a program that cas save a passowed, ans save in a variable
#wenn das von benutzer eingegbe paswort mit dem in variable gespeicherr  passwort uber


saved_password="password1"                 # muster_pasword
pasword= input("Gib deine Passwort ein:")  # user pasword

#saved_password =input("Gib bitte eine passwordt zu spairche:")


if pasword ==saved_password:
    print(saved_password)
    print("du bist bei der VHS eingeloggt")
else:
    print("Fehlermeldung : passwort falch , bitte wiederholen")

#################################

for element in saved_password:
    if saved_password[0]==pasword[0]:
         print("die erste element ist correct ")
         if saved_password[1]==pasword[1]:
             print(" die erste element and the 2 element ")
         else:
            print("die 2 elemnt ist nicgt correct")
         break
    else:
        print("die erste element ist correct")
        break

