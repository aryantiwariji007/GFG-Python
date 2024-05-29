dct={i:i**2 for i in range(1,6)}
print(dct)
print('-'*30)


#dct with conditions
dct={i: i**2 for i in range(1,11) if i%2==0}
print(dct)
print('-'*30)


#Dictionaries with lists
lst=['Apple','Banana','orange']
dct={ item:len(item) for item in lst}
print(lst)
print(dct)
print('-'*30)


dct={ len(item):item for item in lst}
print(lst)
print(dct)
print('-'*30)


#special keys with dct
dct={ 'num_' + str(i):i for i in range(1,101)}
print(dct)

print('-'*30)


#shrtlst based on conditions

dct={ 'num_' + str(i):i for i in range(1,11)}
dct={ k:v for k,v  in dct.items() if v%3==0}
print(dct)

print('-'*30)

lst1=['a','b','c','d']
lst2=[1,2,3,4]

dct={lst2[i]:lst1[i] for i in range(len(lst1))}
print(dct)


#matrix
matrix=[[1,2,3],[4,5,6],[7,8,9]]
final_dct = {(i,j): matrix[i][j]  for i in range(3) for j in range(3)}
print(final_dct)



matrix=[[1,2,3],[4,5,6],[7,8,9]]
final_dct = {matrix[i][j]:(i,j) for i in range(3) for j in range(3)}
print(final_dct)

