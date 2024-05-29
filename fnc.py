
'''
def greet():
    print("Hello")
for i in range(5):
    greet()
print('-'*45) 
def greet():
    print('Hi')
for i in range(5):
    greet()  '''

#Passing the parameters with print

def greet(name):
    return ('Hello', name)
greet('Aryan')    

greet(name='Aryan')
greet()
'''
def subm(a=0,b=0):
    return  a+b
s=subm(5,10)
print(s)

print('-'*45)

#Multi-Return
def arthemetic(a=0,b=0):
    return a+b,a-b,a*b

s=arthemetic(5,8)
print(s)

print(type(s))'''

#Calling different Functions

lst=[1,2,3,4,5]

def sq(lst):
    return[i**2 for i in lst]

def cu(lst):
    return[i**3 for i in lst]


def final(lst):
    lst_1=sq(lst)
    lst_2=cu(lst)

    return  [lst_1[i] + lst_2[i] for i in range(len(lst_1))]
print(sq(lst)) 
print(cu(lst)) 
print(final(lst))  



print('-'*45)









   