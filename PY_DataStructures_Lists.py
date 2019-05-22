# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:01:44 2019

@author: asgupta

working with lists
"""

#basic llist functions
list = [ 'abcd', 786 , 2.23, 'Ram', 70.2 ]
tinylist = [123, 'Ram']

print(list)                # Prints complete list
print(list[0])             # Prints first element of the list
print(list[1:3])           # Prints elements starting from 2nd till 3rd 
print(list[2:])            # Prints elements starting from 3rd element
print(tinylist * 2)        # Prints list two times
print(list + tinylist)     # Prints concatenated lists
print(list.index('Ram'))   # Prints index of an item in list 
print(len(list))           # Prints length of lists

#remove an item from llist
list.remove('Ram')
print(list)
#remove with index
list.pop(1)
print(list)

#some list functions on numbers
numberlist = [1, 5, 23, 1 ,54,2, 54,23, 54,76, 76,34,87]
numberlist.sort()
print(numberlist)
print(len(numberlist))
print(max(numberlist))
print(min(numberlist))

#some more functions on lists
list = ['Ajay', 'Vijay', 'Ramesh']
list.append('Sujay')         
list.insert(0, 'NewGuy')       
list.extend(['Guy1', 'Guy2']) 
print(list)  
print(list.index('Guy1')) 
list.remove('Guy1')
list.pop(1)
print(list)

#string fuctions on lists
string = ['abcd', 'efg', 'hijk', 'lmn']
print(sorted(string, key=len))


#Traversing a list
numbers = [2, 3, 5]
sum = 0
for num in numbers:
    sum += num
print(sum)

#plaing with each item of list
numbers = [2, 3, 5]
getsum = [ i+2 for i in numbers ]
print(getsum)

