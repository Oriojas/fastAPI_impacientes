import pandas as pd

df = pd.read_csv("data/auto_mpg.csv")

columns = df.columns

dict_res = {}

for column in columns:
    try:
        dict_res[f"{column}_max"] = round(df[column].max(), 2)
        dict_res[f"{column}_min"] = round(df[column].min(), 2)
        dict_res[f"{column}_mean"] = round(df[column].mean(), 2)
        dict_res[f"{column}_count"] = df[column].count()
    except:
        dict_res[f"{column}_count"] = df[column].count()

print(dict_res)
