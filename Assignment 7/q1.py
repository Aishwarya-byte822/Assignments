# Practise Pandas Series
# 	Create a Pandas Series from Dictionary

import pandas as pd
data = {
    'Raj':98,
    'Aish':99,
    'Yash':95,
    'Vansh':90
}
my_data=pd.Series(data)
print(my_data)



# Create a Pandas Series from Lists 
import pandas as pd
data = [1,2,3,4,5,8]
s = pd.Series(data)
print(s)



# Access the elements of a Series in Pandas
import pandas as pd 
data =[10,20,30,40]
s = pd.Series(data)

print(s[0])
print(s[2])




