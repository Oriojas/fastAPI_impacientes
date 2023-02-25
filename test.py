import pandas as pd
import data_description as dd
import send_data as sd

URL = "http://0.0.0.0:8088/describe/"

df = pd.read_csv("data/auto_mpg.csv")
# df = df.iloc[0:3]

# des_dict = dd.dataDescription(df=df).fit()

# print(des_dict)

df = sd.sendData(df=df, url=URL).send()

print(df)
