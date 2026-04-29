import pandas as pd


## serie = pd.Series([1, 4, 9], index=['x', 'y', 'z'])

## print(serie)

"""
data = {
    "Nombre": ["Juan", "Ana", "Pedro"],
    "Edad": [25, 30, 35],
}

df = pd.DataFrame(data)

print(df.loc[[0, 2]])
"""  

df = pd.read_csv(r"src\data.csv")

print(df.head(9))