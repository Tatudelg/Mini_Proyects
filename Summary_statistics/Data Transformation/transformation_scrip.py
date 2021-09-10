import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

"""Have to perform some data analysis on the past six months of the company’s 
financial data, which has been loaded in the variable financial_data."""

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

#print(financial_data)

#Store the columns in variables
month = financial_data.Month
revenue = financial_data.Revenue
expenses = financial_data.Expenses

#Plot of revenue over the past six months
plt.plot(month,revenue)
plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Revenue')
plt.show()
#plot of expenses over the past six months:
#Need to use the function plot.clf(). Otherwise, it will be plotted on-top of the revenue plot.
plt.clf()
plt.plot(month,expenses)
plt.xlabel('Month')
plt.ylabel('Amount')
plt.title('Expenses')
plt.show()

"""los ingresos parecen estar disminuyendo rápidamente mientras que los gastos aumentan.  
Si continúa la tendencia actual, los gastos pronto superarán los ingresos."""

#New file to analyze the expenses
expenses_overview = pd.read_csv('expenses.csv')
print(expenses_overview.head())

#Store the columns in variables
expense_categories = expenses_overview.Expense
proportions = expenses_overview.Proportion
#In a pie chart, seems that some categories make up most of the expenses, while the rest of categories make up a small percentage
#Update the pie chart so that all categories making up less than 5% of the overall expenses are collapsed into an “Other” category.
#Calculating the total of the categories with less than 5 percent of proportions
sum_other = sum(proportions[proportions < 0.05])

expense_categories = ['Salaries', 'Advertising', 'Office Rent', 'Other']
proportions = [0.62, 0.15, 0.15, sum_other]

plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expense Categories')
# The pie chart looks deformed, in these lines the axis is established 
plt.axis('Equal')
plt.tight_layout()
plt.show()
#The category more expensive is Salaries

#New file to analyze emloyees productivity
employees = pd.read_csv('employees.csv')
print(employees.head())

#Sort the df by the productivity column in ascending order
sorted_productivity = employees.sort_values(by= ['Productivity'])
print(sorted_productivity)

# Store the first 100 rows of sorted_productivity 
employees_cut = sorted_productivity.head(100)

# Take a look at roughly how long the average commute time is for employees at the company.
commute_times = employees['Commute Time']
print(commute_times.describe())
#The average are 33 minutes and the median 31 minutes

plt.clf()
plt.hist(commute_times)
plt.title('Employees commute times')
plt.xlabel('Commute Time')
plt.ylabel('Frequency')
plt.show()
#The data is right skewed
#How skewed is the data? 1.148400784154177
#print(commute_times.skew())

#Apply the log-transformation to make the data more symetrical
log_commute_times = np.log(commute_times)
#print(log_commute_times.skew())
#Now is the skew is -0.4241330491752042
plt.clf()
plt.hist(log_commute_times)
plt.title('Transformed employees commute times')
plt.xlabel('Commute Time')
plt.ylabel('Frequency')
plt.show()

