# Abraham Aguirre Mendizabal 7I
#list1 = [8,9,6,5,8,9]
#list2 = [8,2,3,6,7,10]

#for i in list1:
#   for j in list2:
#        print(" cruce de lista",i,j)

import os
import sys
from tkinter.ttk import Style
import xlrd
import  xlwt

alumno = ["Francisco","Saul","Rafael","Antonio","Julio"," Efren","sarai","ofelia","Azael","Abigail","Brenda","Carlos","Miguel","Abraham","Oliver","Bruno","Edgar","Eduardo"]
par1 = [7,5,9,6,8,9,8,9,10,8,6,7,8,9,10,9,10,10]
par2 =[7,8,9,10,9,8,8,10,10,7,8,7,8,9,10,8,9,8]
num = len (alumno )
print(num )

lib = xlwt.Workbook()
hoja = lib.add_sheet ("calificaciones")
styleHead = xlwt.easyxf('font: bold I ,color black,height 220;')
styleOrd = xlwt.easyxf('font: bold I,color red;')
def promedio (a,b):
    r = (a + b)/2
    return r
    prom = 0  

for i in range(num):
    for j in range(5):
        if i == 0 and j == 0:
            hoja.write(i,j, " Alumno ")
        elif i == 0 and j == 1:
            hoja.write(i,j, "Primer  parcial")
        elif i == 0 and j == 2:
            hoja.write(i,j, "Segundo  parcial")
        elif i == 0 and j == 3:
            hoja.write(i,j, "Promedio",styleHead)
        elif i == 0 and j == 4:
            hoja.write(i,j, "Presenta:",styleHead)
        elif j == 0:
            hoja.write(i,j, alumno[i-1])
        elif j == 1:
            hoja.write(i,j, par1[i-1])
        elif j == 2:
            hoja.write(i,j, par2[i-1])
        elif j == 3:
            hoja.write(i,j, ((par1[i-1]+par2[i-1])/2))
        elif j == 4:
            if calif < 8:
# si la calificacion es menor a 8 el alumno presenta examen ordinario
                hoja.write(i, j, " Presentas Ordinario")
            elif calif >= 8:
# si la calificacion es mayor a 8 excentas 
                hoja.write(i, j, "Excentas")
                calif = ((par1[i-1]+par2[i-1])/2)
            elif prom < 6 and prom > 0:
                 hoja.write (i,j,"sin derecho",styleOrd) 

lib.save("C:\python\Calificaciones.xls")
