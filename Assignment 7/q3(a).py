# Different ways to iterate over rows in Pandas Dataframe
# using loc
import pandas as pd

data = {
    "qmarks":[420,380,390],
    "duration":[50,40,45]
}

df = pd.DataFrame(data,index=["day1","day2","day3"])

print(df.loc["day2"])


# using iloc
import pandas as pd

df = pd.DataFrame(
    [['a','b'],['c','d'],['e','f'],['g','h']],
    columns=['col1','col2']
)

print(df.iloc[1])

# access multiple rows
import pandas as pd

data = {
    "qmarks":[420,380,390],
    "duration":[50,40,45]
}

df = pd.DataFrame(data)

print(df.loc[[0,1]])