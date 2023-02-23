import pandas as pd
import data_description as dd

df = pd.read_csv("data/auto_mpg.csv")

des_dict = dd.dataDescription(df=df).fit()

print(des_dict)
