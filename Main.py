import pandas as pd
from pandas import ExcelWriter

file1 = pd.read_excel('Files/Archivo1.xlsx', header=None)
file2 = pd.read_excel('Files/Archivo2.xlsx', header=None)
file3 = pd.DataFrame()
file4 = pd.DataFrame()

if(not file1.equals(file2)):
    if(len(file1.index) == len(file2.index)):
        writer1 = ExcelWriter('Files/Archivo3.xlsx')
        for i in file1.index:
            if((file1[0][i]).lower() != (file2 [0][i]).lower()):                                
                file3 = file3.append({'Archivo 1' : file1[0][i],
                                    'Archivo 2' : file2[0][i]},ignore_index=True)
                file3.to_excel(writer1, "Diferente", index=False)
        writer1.save()
    else:
        writer2 = ExcelWriter('Files/Archivo4.xlsx')
        for j in range(len(file1.index), len(file2.index)):
            file4 = file4.append({'No existen en Archivo 1' : (file2[0][j])}, ignore_index=True)
            file4.to_excel(writer2, "Inexistente", index=False)
        writer2.save()
else:
    print("Los archivos son iguales :D")