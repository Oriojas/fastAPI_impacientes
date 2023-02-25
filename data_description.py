class dataDescription:

    def __init__(self, df):
        """
        constructor
        :param df: dataframe, to resume data
        """
        self.df = df
        self.columns = self.df.columns

    def fit(self):
        """
        this function return resume data
        :return: dict, resume data dict
        """

        dict_res = {}

        for column in self.columns:
            try:
                dict_res[f"{column}_max"] = round(self.df[column].max(), 2)
                dict_res[f"{column}_min"] = round(self.df[column].min(), 2)
                dict_res[f"{column}_mean"] = round(self.df[column].mean(), 2)
            except:
                dict_res[f"{column}_count"] = self.df[column].count()

        print(dict_res)

        return dict_res
