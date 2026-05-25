# Make a Pandas DataFrame with a two-dimensional Python list
import pandas as pd
df = pd.DataFrame({
    'Name':['Aish','Raj','Yash','Vansh'],
    'Age':[20,14,18,19],
    'Gender':['Female','Male','Male','Male'],
    'Marks':[99,98,94,95]
})

print(df)


# Create DataFrame from Python dict
import pandas as pd
df = pd.DataFrame({ 'Name':['Aish','Raj','Yash','Vansh'],
 'Age':[20,14,18,19], 
 'Gender':['Female','Male','Male','Male'], 
 'Marks':[99,98,94,95] })
print(df)




# Create Pandas dataframe using list of lists

import pandas as pd
data = [
    ['Aish',20,'Female',99],
    ['Raj',14,'Male',98],
    ['Yash',18,'Male',94],
    ['Vansh',19,'Male',95]
]
df = pd.DataFrame(data,columns=['Name','Age','Gender','Marks']
)

print(df)




# Create a Pandas dataframe using list of tuples 

import pandas as pd

data = [
    ('Aish',20,'Female',99),
    ('Raj',14,'Male',98),
    ('Yash',18,'Male',94),
    ('Vansh',19,'Male',95)
]

df = pd.DataFrame(
    data,
    columns=['Name','Age','Gender','Marks']
)

print(df)
