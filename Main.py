import pandas as pd
from pandas import ExcelWriter

#Leemos los archivos excel como data frames
file1 = pd.read_excel('Files/Archivo1.xlsx', header = None)
file2 = pd.read_excel('Files/Archivo2.xlsx', header = None)

#Creamos data frames vacíos
file3 = pd.DataFrame()
file4 = pd.DataFrame()

#Hallamos el minimo número de filas de los archivos
min = min(len(file1.index), len(file2.index))

#Comparamos la igualdad de las celdas en minúsculas
for i in range(min):
    if((file1[0][i]).lower() == (file2[0][i]).lower()):
        sameFiles = True
    else:
        sameFiles = False

if(not(file1.equals(file2) and sameFiles)):
    #Se crea el archivo 3
    for i in range(min):
        if((file1[0][i]).lower() != (file2 [0][i]).lower()):                                
            writer1 = ExcelWriter('Files/Archivo3.xlsx')
            file3 = file3.append({'Archivo 1' : file1[0][i], 'Archivo 2' : file2[0][i]}, ignore_index = True)
            file3.to_excel(writer1, "Diferente", index = False)
            writer1.save()
    
    if(file3.empty):
        print("No hay diferencias en las primeras", min, "filas")
    else:
        print(file3)

    #Se crea el archivo 4     
    if(len(file2.index) > len(file1.index)):
        writer2 = ExcelWriter('Files/Archivo4.xlsx')
        for j in range(len(file1.index), len(file2.index)):
            file4 = file4.append({'No existen en Archivo 1' : (file2[0][j])}, ignore_index = True)
            file4.to_excel(writer2, "Inexistente", index = False)
        writer2.save()
        print(file4)
            
else:
    print("Los archivos son iguales :D")