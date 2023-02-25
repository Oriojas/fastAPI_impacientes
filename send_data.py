import json
import requests
import pandas as pd


class sendData:

    def __init__(self, df, url):
        self.url = url
        self.df = df

    def send(self):

        df = self.df.dropna()
        data = df.to_dict(orient="records")
        data_dumps = json.dumps(data)
        response = requests.post(url=self.url, data=data_dumps)

        res_json = eval(response.json())

        df_output = pd.DataFrame(list(res_json.items()),
                                 columns=['Name', 'Value'])

        return df_output
