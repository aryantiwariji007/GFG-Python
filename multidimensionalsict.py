dct={1:{'name':'Aryan','phone':[9752,261092]},
2:{'name':'Atul','phone':97522610923}}
print(dct)
print('-'*45)

#Accessing the elements
print(dct)
print(dct[2]['name'])
print('-'*45)

#updating
print(dct)
dct[2]['name']='Kapil'
print(dct)
print('-'*45)
#adding
print(dct)
dct[3]={'name':'Akshat','phone':[9752,2899]}
print(dct)
print('-'*45)

#deleting
print(dct)
del dct[3]
print(dct)
print('-'*45)

#Going through the data
print(dct)

for i in dct.keys():
    print(i,dct[i]['name'],dct[i]['phone'])
    print(dct)
print('-'*45)

