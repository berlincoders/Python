#schreiben sie eine function die
#

#pi*radius**2

def circle(radius):
    pi=3.1416
    output=(pi*radius)**2
    print(output)
    return pi*radius**2

circle(3)


#print(type(circle(5)))
###### interesante con return el tipo de dato no es desconociod


## schreiben sie eine weitere Funktion, die das volumen eines zilinder unter
#verwerdun  der obigen Funktion , 2 parameter
#r, h
#vol_zyl=flache_kreis*h


def zyl_vol(radius,h):
    vol_z=circle(radius)*h  ### el parametro tiene que estar incluido
    print(vol_z)   # Imprime en pantalla
    return vol_z   # return a value

zyl_vol(3,5)













