import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import codecademylib3_seaborn
import glob
#Código viejo para cargar usando istas
"""#Concatenamos los files
files = glob.glob("states*.csv")
census_list = []
for filestates in files:
  #Si establecemos index_col=0, estamos indicando explícitamente que tratemos la primera columna como el índice
  data = pd.read_csv(filestates, index_col = 0)
  census_list.append(data)

us_census = pd.concat(census_list)"""

#Concatenamos los files
files = glob.glob("states*.csv")
# no crea una lista, ni se agrega a una
df_from_each_file = (pd.read_csv(f) for f in files)
us_census = pd.concat(df_from_each_file, ignore_index=True)

#Borramos la columna de index vieja
us_census= us_census.drop(['Unnamed: 0'], axis = 1)

#Sacamos el $ de Income para transformarlo a columna de tipo numérico
us_census.Income = us_census['Income'].replace('[\$]',"", regex = True)
us_census.Income = pd.to_numeric(us_census.Income)

#print(us_census.GenderPop.head())
#Hay que dividir los datos de los géneros
#split para separar desde _, en una nueva columna
us_census['gender_split'] = us_census.GenderPop.str.split('_')
#Creamos las nuevas columnas de Women y Men
us_census['Women'] = us_census.gender_split.str.get(1)
us_census['Men'] = us_census.gender_split.str.get(0)

#Dejamos solo los números
us_census.Women = us_census['Women'].replace('F',"", regex = True)
us_census.Men = us_census['Men'].replace('M',"", regex = True)

#Convertimos las columnas a números
us_census.Women = pd.to_numeric(us_census.Women)
us_census.Men = pd.to_numeric(us_census.Men)
#Completamos los valores nan de Women con la resta entre TotalPop y Men
us_census = us_census.fillna(value = {"Women": us_census.TotalPop - us_census.Men})

#Chequeamos que estén ok los types
#print(us_census.head())
print(us_census.dtypes)
#borramos gender_split y GenderPop
us_census = us_census.drop(['gender_split', 'GenderPop'], axis = 1)
#print(us_census.Women)

#chequeamos y borramos duplicados
duplicates = us_census.duplicated()
#print(duplicates)
#borramos valores duplicados
#Reseteamos el index por el drop duplicates
us_census = us_census.drop_duplicates().reset_index(drop = True)

#grafico
"""plt.scatter(us_census.Women, us_census.Income) 
plt.show()"""

print(us_census.columns)
#st_tp = us_census[['State', 'TotalPop']]
#Histograma
plt.hist(us_census.State, us_census.TotalPop, bins= range(max(us_census.TotalPop))) 
#plt.hist(data, bins=range(min(data), max(data) + binwidth, binwidth))
# x = us_census['State'], y= us_census['TotalPop'],
# generamos el histograma a partir de los datos

plt.show()

