import pandas as pd

path = 'Data/test.csv'

df = pd.read_csv(path)

print(df.head())