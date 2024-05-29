my_set={1,2,3,4,5}
print(my_set)
print(type(my_set))
print('-'*45)

#Adding
print(my_set)
my_set.add(7)
print(my_set)
print('-'*45)



#pop
print(my_set)
popped_element= my_set.pop()
print(popped_element)
print('-'*45)



#Remove
print(my_set)
my_set.discard(5)
print(my_set)
print('-'*45)

#iterating
print(my_set)
for i in my_set:
    print(i)
print('-'*45)

#checking the value
print(2 in my_set)
print(9 in my_set)
print(my_set)
print('-'*45)

#Set Opertions
set_1={1,2,3,4,5}
set_2={4,5,6,7,8}
print("Union:",set_1 | set_2)
print("Itersection:",set_1 & set_2)
print("diference:",set_1 - set_2)
print("difference:",set_2 - set_1)

print("Symmetric Diff:",set_1 ^ set_2)
print('-'*45)

#Clearing
print(my_set)
my_set.clear()
print(my_set)
print('-'*45)



#touple initialization
tpl=(2,3,4,5,6,7,8)
print(tpl)

#slicing
tpl=(1,2,3,4,5)
print(tpl[2:3])

print('-'*45)

#concatenate
tpl_1=(1,2,3,4,5)
tpl_2=(4,5,6,7)
tpl = tpl_1 + tpl_2
print(tpl)
print('-'*45)

#iterating
print(tpl)
for i in tpl:
    print(i)
print('-'*45)   

#Checking the count
print(tpl)
print(tpl.count(4))
print('-'*45)   

#multiplying the tuple
print(tpl)
print(tpl*3)




