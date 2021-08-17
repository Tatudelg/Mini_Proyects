import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

#Create a table of frequencies of all the cars reviewed by manufacturer_country.
table_freq = car_eval['manufacturer_country'].value_counts()
print(f"{table_freq.index[1]} is the modal category.")
print(f"{table_freq.index[4]} appears 4th most frequently")

#Calculate a table of proportions for countries that appear in manufacturer_country in the dataset
table_prop = car_eval['manufacturer_country'].value_counts(normalize = True)
print(table_prop)
print(f"The {table_prop['Japan']} of cars were manufatured in Japan")

#Print out a list of the possible values for buying_cost
print(car_eval["buying_cost"].unique())

#Create a new list that contains the unique values in buying_cost,
buying_cost_categories = ['low', 'med', 'high', 'vhigh']
#Convert buying_cost to type 'category'
car_eval['buying_cost'] = pd.Categorical(car_eval['buying_cost'], buying_cost_categories, ordered = True)
#Calculate the median category of the buying_cost 
median_index = np.median(car_eval['buying_cost'].cat.codes)
median_category = buying_cost_categories[int(median_index)]
print(median_category)

#Calculate a table of proportions for the luggage variable
table_prop_luggage = car_eval['luggage'].value_counts(dropna = True, normalize = True)
print(table_prop_luggage)
#Are there any missing values in this column? Replicate the table of proportions from the previous exercise, but do not drop any missing values from the count
table_prop_luggage1 = car_eval['luggage'].value_counts(dropna = False, normalize = True)
print(table_prop_luggage1)
#Without passing normalize = True to .value_counts(), can you replicate the result you got in the previous exercises?
table_prop_luggage2 = car_eval['luggage'].value_counts() / len(car_eval['luggage'])
print(table_prop_luggage2)

#Find the count of cars that have 5 or more doors.
more5_doors_frequency = (car_eval['doors'] == '5more').sum()
print(more5_doors_frequency)
#Find the proportion of cars that have 5+ doors and print the result.
more5_doors_proportion = (car_eval['doors'] == '5more').mean()
print(more5_doors_proportion)

