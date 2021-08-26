import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import codecademylib3

# load in the data
df = pd.read_csv("mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()
for column in columns:
  #print(column)
  # Turn any bar graph with less than six bars into a pie chart
  dif_values = len(list(df[column].unique()))
  if dif_values < 6:
    widge_sizes = df[column].value_counts()
    grade_labels = df[column].unique()
    plt.pie(widge_sizes, labels = grade_labels)
    plt.axis('equal')
  
  else:
    sns.countplot(df[column], order = df[column].value_counts().index)  
    # rotates the value labels slightly so they don’t overlap, also slightly increases font size
    plt.xticks(rotation=30, fontsize=10)
    # increases the variable label font size slightly to increase readability
    plt.xlabel(column, fontsize=12)
  plt.title(column + " Value Counts")
  plt.show()
  plt.clf()

