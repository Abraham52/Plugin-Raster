import sys 
import keyword
import operator
import os

#print(keyword.kwlist)
#print(len(keyword.kwlist))

lvar=10
# comentario 
""" multiple comentario"""
#Identacion 
p = 10 
if p == 10 :
    print(' p is igual a 10 ')

# Variable
o = 5
id(o)

id(p)

p = 20
q = 20
r =q
#Tuplas --->no permiten cambios en sus valores ()
mi_tupla = ( 1,2,3,4,5,'tupla')
            #0,1,2,3,4,5
print (mi_tupla[1])


# listas --> permiten cambios [] 
lista = [6,7,8,9,10,'python']
print (lista[4:])
# Diccionarios --> permiten cambios {}
dic ={'uno':1,'dos':2,'tres':3,'cuatro':4,'cinco':5}
dic ['tres']= 6 # cambio valores 
print(dic['tres'])