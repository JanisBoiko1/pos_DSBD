import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
dataset = pd.read_csv(url, sep='\t')

print(dataset.head())

print(dataset.dtypes)

print(dataset.info())

df_item_quantidade = dataset[['item_name', 'quantity']].copy
print(df_item_quantidade)