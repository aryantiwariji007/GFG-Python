

#exception handling
'''

try:

    x=10
    print(1)
    print(x/0)
    print(2)
except:
    print("error occured!")'''


#exception with specific errors
'''
try:
    num=0
    print(int('e23'))
except ZeroDivisionError:
    print('Zero in the division')

except:
    print('Unknown error!')        

'''
#Final exception with specific errors
try:
    num1, num2=10,5
    
    print(num1/num2)

except ZeroDivisionError as zde:
    print(zde)
except exception as e:
    print(e)
else:
    print("everything is fine!")

finally:
    print('Program ends!')            