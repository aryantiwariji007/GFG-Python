lst=['Aryan',1,7.90,True]
print(lst)
print(lst[-1])
print('-'*34)

lst[0]='Atul'
print(lst)
print('-'*34)

#slicing
print(lst[1:3])
print('-'*34)

#Reverse a string
print(lst[::-2])
print('-'*34)

#appending
lst=['Aryan',1,7.90,True]
print(lst)
lst.append("ankit")
print(lst)

#removing an element
lst.remove('ankit')
print(lst)
print('-'*34)
#length
print(lst)
print(len(lst))

print('-'*34)

#Sorting
lst=[3,65,5,4,7,1,4,6,7]
print(lst)
print(sorted(lst))
print('-'*34)

#find element
lst=['aryan','atul','akshat']
print(lst.index('akshat'))

#count(tells the frequency of data)
lst=['aryan','atul','akshat']
print(lst.count('akshat'))

#extending
lst=['aryan','atul','akshat']
lst.extend(['aysha','astha'])
print(lst)

#Finding max and min of list

lst=[3,6,4,7,9,6,2200,6]
print(lst)
print(max(lst))
print(min(lst))
print('-'*34)

#iterting through the elements of list

lst=[3,6,4,7,9,6,2200,6]
print(lst)
for i in range(len(lst)-1,-1,-1):
    print(lst(i))
print('-'*34)




