from os import write
import pandas as pd
from pandas import ExcelWriter

file1 = pd.read_excel('Files/Archivo1.xlsx', header=None)
file2 = pd.read_excel('Files/Archivo2.xlsx', header=None)
file3 = pd.DataFrame()

if(not file1.equals(file2)):
    writer1 = ExcelWriter('Files/Archivo3.xlsx')
    for i in file1.index:
        if(file1[0][i] != file2 [0][i]):
                                
            file3 = file3.append({'Archivo 1' : file1[0][i],
                                  'Archivo 2' : file2[0][i]},ignore_index=True)
            file3.to_excel(writer1, "Diferente", index=False)
    writer1.save()

print(file1)