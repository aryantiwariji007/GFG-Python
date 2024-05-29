#zip

lst1=['Aryan','Pratham',' Atul']
lst2=[45,78,67]
print(list(zip(lst1,lst2)))
print('-'*45)


matrix=[[1,2,3],[4,5,6],[7,8,9]]
print([list(row) for row in zip(matrix)])
print([list(row) for row in zip(*matrix)])
print([list(row) for row in zip(*[list(row) for row in zip(*matrix)])])
print('-'*45)

#filter


lst=[1,2,3,4,5,6,7,8]
def is_even(n):
    return n%2==0
print(list(filter(is_even,lst)))
print('*'*45)

#Lambda


add_num=lambda x,y : x*y
print(add_num(5,10))
print('-'*45)

num=[1,2,3,4,5,6,7,8,9]
print(list(filter(lambda x: x%2==0,num)))
print('-'*45)



#Map


num=[1,2,3,4,5,6]
def sqr(x):
    return x**2
print(list(map(sqr,num)))

names=['Aryan','Ashi','Atul','Akshat']

print(list(map(lambda x: len(x),names)))