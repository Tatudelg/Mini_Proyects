import pandas as pd
pd.set_option('display.max_colwidth', -1)
df = pd.read_csv("jeopardy.csv")
#Renombro las columnas
df.columns = ['Show Number', 'Air Date', 'Round', 'Category', 'Value', 'Question', 'Answer']

#Muestro todas las columnas, tenían espacios
pd.options.display.max_columns = None


# Write a function that filters the dataset for questions that contains all of the words in a list of words.
def filter(dataset, words):
  #lower para que todas sean iguales
  funcion = lambda x: all(word.lower() in x.lower() for word in words)  
  # Applies the labmda function to the Question column and returns the rows where the function returned True
  return dataset.loc[dataset["Question"].apply(funcion)]

probando_filter = filter(df, ["king", "england"])
#print(probando_filter)

# Adding a new column. If the value of the float column is not "None", then we cut off the first character (which is a dollar sign), and replace all commas with nothing, and then cast that value to a float. If the answer was "None", then we just enter a 0.
df['Float Value'] = df["Value"].apply(lambda x: float(x[1:].replace(',','')) if x != "None" else 0)

# Filtering the dataset and finding the average value of those questions
filtered = filter(df, ["King"])
print(filtered["Float Value"].mean())
