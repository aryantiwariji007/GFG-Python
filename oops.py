class person:
    name='Aryan'
    age='20'
p1=person()
print(p1.name)
print(p1.age)

print('-'*45)

p1.name='stuti'
p1.age='21'

print(p1.name)
print(p1.age)

p2=person()
print(p2.name)
print(p2.age)
print('*'*45 )

class mathematics:
    name='Aryan'

    def greet(self):
        print('Hello')
        return 'Hi'

    def factorial(self,n):
        s=1
        for i in range(n+1):
            s*=i 
        return s   

    def lst_mul(self,lst):
        s=1
       for i in lst:
        s*=i
        return self

    def lst_dot(self,lst_1,lst_2):
        return[lst_1[i]*lst_2[i]]  for i in range(len(lst_1))       

       
math = mathematics()
print(math.greet())

print(math.factorial(5))




print('-'*45)



