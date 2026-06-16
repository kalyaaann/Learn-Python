import pandas as pd
import numpy as np
#know version of pandas installed

print(pd.__version__)

#create a dataframe
# using a List
df = pd.DataFrame([1,2,3,4], columns=['Column Name'])
print(df)

# # check data type
print(type(df)) 

# # using Dictionary 
data = {
    'Name': ['Kalyan', 'Ishan', 'Rohit', 'Sandeep'],
    'Age': [19,18,24,21],
    'Salary': [100000, 25550, 15000, 20000]
}
df = pd.DataFrame(data)
print(df)
print(type(df))

# #Basic DataFrame Understanding 

print(df.head(2)) # top rows
print(df.tail(2)) # last 2 rows
print(df.shape) #gives the table dimensions. rows*columns
print(df.columns) # gives the list of columns in dataframe along with datatype 
print(df.rename(columns={'Name': 'First_Name'})) #changes column name 
print(df)
df.rename(columns={'Name': 'First_Name'},inplace=True) #changes column name and changes in dataframe
print(df)
print(df.info()) #prints the information about the dataframe
print(df.describe()) # describe method generates descriptive statistics of DataFrame, only for numerical-value columns

#Save and Load Data from CSV
df.to_csv('testdata.csv',index=False) #export dataframe 
loaddf=pd.read_csv('testdata.csv')    #import dataframe

print(loaddf)


#rows column selection 
# select single column
print(df[['Name']])
# select multiple columns
print(df[['Name', 'Salary']])
# select single row for specific 
print(df.loc[df.Name=='Kalyan'])
# select multiple rows || loc - label based index
print(df.loc[(df.Name=='Ishan') & (df.Salary>=20000)])
#indexing table
print(df.iloc[0])
print(df.iloc[0:2]) # [start:stop:step]

# filter and store dataframe in a new variable

df_age_filter = df[df['Age'] >= 21] 
print(df_age_filter)
# multiple filter conditions
print(df[(df['Age'] >= 21) & (df['Salary'] >= 19000)]) 
# where function replace values in a DataFrame based on a condition
print(df.where(df['Age'] >= 21)) 
#doesnot change the dimension of the dataframes. 
#other parameter adds the custom texts to the dataframe.
print(df.where(df['Age'] >= 21, other = 'Not Eligible')) 

#rows and columns 
# Create a new column
df['College'] = ['PNC', 'PNC', 'MAC', 'SOCH']
print(df)
# Add new columns using existing column/s
df['Bonus'] = df['Salary'] * 0.5
print(df)
# Add new row - at the end of dataframe
df.loc[len(df)] = ['Sudip', 21, 21000, 'IT', 2000]
print(df)
# update value in dataframe using index-name
df.loc[0, 'Salary'] = 20000
print(df)
# update value in dataframe using column-value
df.loc[df.Name=='Kalyan','Salary'] = 100000
print(df)


# delete value - rows and columns

#delete row using column-value filter
df = df.drop(df[df.Name == 'Sudip'].index) 
print(df)
#delete row using index-name filter
del_col = df.drop('Age', axis=1)
print(del_col)

df.drop(['Name', 'Salary'], axis=1, inplace=True) # delete multiple columns

#sort values - order values in dataframe by asc or desc order
sort_df=df.sort_values('Salary') #ascending order, by default
print(sort_df)
# sort values in descending order
des_sort=df.sort_values('Salary', ascending=False)
print(des_sort)

df['Age'] = ['19', '18', '25', '22']
print(df)

#Working with dates
# create a date column - date of joining
df['DOJ'] = ['2024-01-01', '2024-01-15', '2024-03-28', '2024-03-03']
print(df)

print(df['DOJ'].dtype) # strings
df['DOJ'] = pd.to_datetime(df['DOJ']) # change to date-time type
print(df['DOJ'].dtype) # date-time type



#null and missing values 
print(df.isnull())
df.loc[df.Name=='Kalyan', 'Salary'] = np.nan # adding a null value
print(df)
print(df.isnull())
print(df.isnull().sum() ) #counts all the null values by column 
print(df.fillna(0))
df.loc[df.Name=='Kalyan', 'Salary'] = 30000
print(df)

#Aggregation and groupby 
# frequency of values in month column
print(df['Name'].value_counts())
print(df['Age'].value_counts())
#groupby
print(df.groupby('Salary')['Age'].sum()) 

#Concatenate and Merge Dataframes (JOINS)

df1 = pd.DataFrame({'ID':[1,2,3],'Name':['A','B','C']})
print(df1)
df2 = pd.DataFrame({'ID':[1,2,2,4],'Score':[88,96,77,79]})
print(df2)
# Concatenate: vertical / row level / top on top
print(pd.concat([df1, df2], axis=0))

# Concatenate: horizontal / column level / side on side
print(pd.concat([df1, df2], axis=1))

# merge = join
print(pd.merge(df1, df2, how='inner', on='ID'))




