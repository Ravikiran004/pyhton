# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 10:22:03 2023

@author: Ravikiarn
"""

lst=[1,2,3,4,5,'sanket']
lst.append(3)
print(lst)
lst.extend(['vishwjit','ravikiran'])
print(lst)
lst.remove('vishwjit')
lst
len(lst)
lst.count('ravikiran')
###################################
dic={1:'ravi',2:'pratik',3:'vishwjit'}
for i in dic:
    print(i,dic[i])
dic[4]='ravikiran'
dic
dic[3]='tambe'
dic
dic.items()
#######################################
tup=(1,2,3,4,'pratik','vishwjit')
tup.count(1)
len(tup)
tup.index('pratik')
##########################################
sett={1,3,4,5,6,'pratik'}
sett.add(87)
sett
sett.update({11,12,14})
sett
sett.remove('pratik')
sett
######################################
#Function
def add_sum(a,b):
    return a+b
add_sum(3, 4)
##############################
def adding(b,a=3):
    return b+a
adding(4)
############################
def add_one(a=1,b=2):
    return a+b
add_one(1,7)
###############################
import json 
filename='username.json'
i=input('enter your name:')
with open(filename,'w') as fo:
    json.dump(i,fo)

with open(filename) as fo:
    name=json.load(fo)
print(f"{name}")
###############################
def splitted_string(func):
    def wrapper():
        funct=func()
        splitted=funct.split()
        return splitted
    return wrapper

#########################
@splitted_string
def say_hi():
    return 'Good morning'
say_hi()   
############################
technologies1={
    'courses':["spark","Java","Python","Go"],
    'Discount':[2000,2300,1200,2000]
    }

del technologies1['Discount'][2]
technologies1
###################################
del technologies1['courses'][1]
technologies1




















