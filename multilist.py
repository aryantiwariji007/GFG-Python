lst=[[1,2,3],[4,5,6],[7,8,9]]
print(lst)
#accessing the element

print(lst[2][2])
print("-"*45)
#modify the values
lst[1][1]=9
print(lst)
lst[0]=['ARYAN',19]
print(lst)
print("-"*45)


#Appending the values
lst=[[1,2,3],[4,5,6],[7,8,9]]
print(lst)

lst.append([12,10,11])
print(lst)
print("-"*45)

#Delete the INdex
print(lst)
del lst[0] 
print(lst)
print("-"*45)
#Modify the values
lst=[1,2,3,4,5,[1,2,3],6]
print(lst)
print(len(lst))
print("-"*45)

#Reverse

lst=[[1,2,3],[4,5,6],[7,8,9]]
print(lst)
print(lst[::-1])
print("-"*45)

#accessing all elements
print(lst)
for i in lst:
    for j in i:
        print(j)