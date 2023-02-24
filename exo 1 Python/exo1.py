import pandas as pd

counter = 0

df = pd.read_csv('/Users/theorobert/Desktop/scrapping/dc5b_clean_td_ROBERT_Theo/exo 1 Python/electronic-card-transactions-december-2022-csv-tables.csv', header=0, sep=',')
print(df.head(20))
