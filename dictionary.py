


dct={1:"Aryan",2:"Aysha",3:"Ashi",2:"Astha",'1':'Akshat'}
print(dct)
print('-'*45)

#Acessing the elements
print(dct)
print(dct[1])
print(dct.get(2))


#Adding and updating the key value pair

print(dct)
dct[2]="Atul"
print(dct)
del dct[3]
print(dct)
print('-'*45)
#cleaning the Dictionary

print(dct)
dct.clear()
print(dct)
print('-'*45)
#Iterating through the dct
dct={1:"Aryan",2:"Aysha",3:"Ashi",2:"Astha",'1':'Akshat'}
print(dct)
print(dct.keys())
print(dct.values())
print('-'*45)

for i in dct.keys():
    print(i,dct[i])

    print('-'*45)

    print(dct.items())
    for k,v in dct.items():
        print(k,v)
 print('-'*45)

 #Check if key is present


#merging the dictionaries
dct_1={1:'A',2:'B',3:'C'}
dct_2={1:a,2:'b',3:'c'}
dct_1.update(dct_2)
print(dct_1)



