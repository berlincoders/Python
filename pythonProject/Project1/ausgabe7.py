#gegebn ist eine liste von Zahlen , zäale wie häufig di 5 darin, nu
#nutze eine for -schelife
nums=[1,5,3,5,1,9,5,8,6,5]#5


#lange=len(nums)  #10
#counter=nums[0]### wie wile 5
#counter=0


#for el in nums:   ###
#    print(el)     ## test
#    if el == 5:
#        counter=counter+1
#        print("es ist 5")

#print(counter)


########
def zähl_zäahl_in_liste(zahl,liste):
    ## wie oft zahl in der liste vorkommt
   count=0
   for el in liste:
       if el==zahl:
           count=count+1
print (count)




zähl_zäahl_in_liste(5,nums)




