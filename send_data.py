import json
import requests
import pandas as pd


class sendData:

    def __init__(self, df, url):
        """
        constructor
        :param df: dataframe, to send endpoint
        :param url: str, url service endpoint
        """
        self.url = url
        self.df = df

    def send(self):
        """
        this method sends data to the endpoint
        :return:
        """

        df = self.df.dropna()
        data = df.to_dict(orient="records")
        data_dumps = json.dumps(data)
        response = requests.post(url=self.url, data=data_dumps)

        res_json = eval(response.json())

        df_output = pd.DataFrame(list(res_json.items()),
                                 columns=['Name', 'Value'])

        return df_output
