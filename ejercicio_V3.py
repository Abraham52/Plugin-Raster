# Trabajando con conjunto 

A = {1,2,3,4,5}
B = { 4,5,6,7,8}
C = { 8,9,10}

# union de conjuntos 
A | B

R = A.union(B)
print(R)
R= A.union(B,C)
print(R)

# interseccion de conjuntos 
R = A.intersection(B)
print(R)

# Diferencia de conjuntos
R = A.difference(B)
print(R)
