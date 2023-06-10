my_mine=[1,"Apfel",["mine1",2,"mine2",["Gold","SILVER"]],3,True,"foo"]


#Aufgabe : holen sie das gold raus, wo genaw das gold (stelle , index)
#print output ->gold

partial_gold=my_mine[2]
second_partial_gold=partial_gold[3]
gold= second_partial_gold[0]

print(gold)

my_mine2=[1,"Apfel",["mine1",2,"mine2",["Golderivation","silver"]],3,True,"FOO"]

p_gold=my_mine2[2]
p2_gold=p_gold[3]
p3_gold=p2_gold[0]
gold=p3_gold[0:4]



output3=my_mine2[2][3][0][0:4]

print(gold)


output2=my_mine[2][3][0]

print(output2)
print(output3)