lst=[1,2,3,4,5]
print(lst)
lst=[i**2 for i in lst]
print(lst)
lst=[i**2 for i in lst]
print(lst)
lst=[i for i in lst if i%2==0]
print(lst)
print('-'*45)

#Finding first 10 even nos
lst=[i for i in range(21) if i%2==0 ]
print(lst)
print('-'*45)
#Multi-dimensional lists

#

#accessing all the elements of a list
lst=[[1,2,3],[4,5,6],[7,8,9]]
print(lst)
print([j for i in lst for j in i])
