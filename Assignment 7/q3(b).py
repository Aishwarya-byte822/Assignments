# Selecting rows in pandas DataFrame based on conditions 
import pandas as pd

df = pd.DataFrame({
    'Product':['Laptop','Phone','Tablet','Monitor'],
    'Price':[55000,25000,18000,12000],
    'Stock':[10,0,5,2]
})
result = df[df['Price'] > 20000]
print(result)

result = df[df['Stock'] > 0]
print(result)

result = df[(df['Price'] > 15000) & (df['Stock'] > 0)]

print(result)




# Select any row from a Dataframe using iloc[]
import pandas as pd

df = pd.DataFrame({
    'Name':['Aish','Raj','Yash','Vansh'],
    'Marks':[99,85,92,70]
})

result = df.iloc[2]

print(result)



# Limited rows selection with given column
import pandas as pd

df = pd.DataFrame({
    'Name':['Aish','Raj','Yash','Vansh'],
    'Marks':[99,85,92,39],
    'Age':[20,18,19,17]
})
result = df.loc[0:1, 'Name']

print(result)


# Drop rows from the dataframe based on certain condition applied on a column 
result = df[df['Marks'] >= 50]

print(result)


# Insert row at given position in Pandas Dataframe
import pandas as pd

df = pd.DataFrame({
    'Name':['Aish','Raj','Vansh'],
    'Marks':[99,85,70]
})
df.loc[3] = ['Yash',92]

print(df)


# Create a list from rows in Pandas DataFrame
import pandas as pd

df = pd.DataFrame({
    'Name':['Aish','Raj','Yash'],
    'Marks':[99,85,92]
})
result = df.values.tolist()

print(result)