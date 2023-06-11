
#create and call a function
def say_hi(name,age):
    print(" Hellow "+ name +", you are "+ age )

say_hi("Romeo","35")
say_hi("Mike","40")

def cube(num):
     return num*num*num

result = cube(4)
print(result)
##########################


#def func_name(some_parameter):
#    output=some_parameter*4
#    print(output)  # un parametro puede ser cualquier tipo de dato

#func_name(5)
############################
#def func_name(some_parameter=100):#  si se llama a la funcion el parametro es 100, por defecto
#    output=some_parameter*4
#    print(output)  # un parametro puede ser cualquier tipo de dato

#func_name()       # como no defino el parametromcojo por defecto el que aparece por defecto

def berechhne_len (something):
    print(len(something))

berechhne_len("Iche lerne bei der VHS")
berechhne_len([1,2,3,"hallo",True])















