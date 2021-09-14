import pandas as pd
import numpy as np

diabetes_data = pd.read_csv('diabetes.csv')
#print(diabetes_data.head())

#Print the full dimensions of the data
#print(diabetes_data.shape)
#768 rows, 9 columns

#Verifying null values
print(diabetes_data.isnull().sum()) #0
print(diabetes_data.info())
#Apparently there is not null values, but are there missing values?
print(diabetes_data.describe())
"""The minimum values for Glucose, BloodPressure, SkinThickness, Insulin and BMI
are 0. These values also seem to be way off from their respective medians and means, another indicator that something is off.
We can interpret that these are missing values.
The maximum value of the Insulin column is 846, which is abnormally high.
The maximum value of the Pregnancies column is 17. This case might be something to look further into to determine its accuracy.
 """

 #Replace the instances of 0 with NaN
diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)
#Check missing values
print(diabetes_data.isnull().sum())
print(diabetes_data.info())

#Print null values
print('nullvalues', diabetes_data[diabetes_data.isnull().any(axis=1)])
"""Most rows with missing data have missing values in more than one column. In fact, every single row with at least one missing value 
also has a missing value in the insulin column."""

print(diabetes_data.dtypes)
print(diabetes_data.Outcome.unique())
"""We have instances of the character 'O' in addition to the number 0.
The documentation tells us that the value of the Outcome column should 
either be a 0 or a 1, so it seems likely that instances of the character 'O' are misentries"""
diabetes_data.Outcome = diabetes_data.Outcome.replace('O', 0)
diabetes_data.Outcome = pd.to_numeric(diabetes_data.Outcome)

print(diabetes_data.Outcome.unique())

#replacing the values with the mean of each column.
#Does not work :c
"""columns_with_null_values = (diabetes_data.Glucose, diabetes_data.BloodPressure, diabetes_data.SkinThickness, diabetes_data.Insulin, diabetes_data.BMI)
for column in columns_with_null_values:

    column = column.fillna(np.mean(column))

print(diabetes_data[diabetes_data.isnull().any(axis=1)])
print(diabetes_data.isnull().sum())"""
