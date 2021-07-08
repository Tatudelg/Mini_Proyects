import codecademylib3_seaborn
from bs4 import BeautifulSoup as BS
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


webpage = requests.get("https://content.codecademy.com/courses/beautifulsoup/cacao/index.html")
web = webpage.content
soup = BS(web, "html.parser")

#Busco los ratings por su etiqueta
cant_chocolates = soup.find_all(attrs ={"class":"Rating"})
ratings = []
#print (cant_chocolates)

#Itero por los ratings para guardar solo las calificaciones en una lista, salteo el 0 porque es el nombre de la columna
for rating in cant_chocolates[1:]:
  ratings.append(float(rating.get_text()))
  
print(ratings)
#Uso matplotlib
plt.hist(ratings)
#plt.show()

#Busco nombres de las compañías 
nom_company = soup.select(".Company")
company_list = []
#Itero para guardaslas en la lista
for name in nom_company[1:]:
  company_list.append(name.get_text())

#Busco porcentajes de cacao 
cocoa_percent = soup.select(".CocoaPercent")
cocoa_list = []
#Itero para guardaslas en la lista
for percent in cocoa_percent[1:]:
  per1 = int(float((percent.get_text()).strip('%')))
  cocoa_list.append(per1)

#Creo un DF con las listas
df = {'Company Name' : company_list, 'Rating':ratings, 'Cocoapercent' : cocoa_list}
chocolate_df = pd.DataFrame.from_dict(df)

# Guardo los promedios de las calificaciones por compañía
mini_df = chocolate_df.groupby('Company Name').Rating.mean()
#Imprimo los 10 mejores
print(mini_df.nlargest(10))


plt.scatter(chocolate_df.Cocoapercent, chocolate_df.Rating)
z = np.polyfit(chocolate_df.Cocoapercent, chocolate_df.Rating, 1)
line_function = np.poly1d(z)
plt.plot(chocolate_df.Cocoapercent, line_function(chocolate_df.Cocoapercent), "r--")
plt.show()
plt.clf()
