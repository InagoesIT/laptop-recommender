import pandas as pd

from pathlib import Path


class LaptopFilter:
    def __init__(self, file_name):
        self.df = pd.read_csv(file_name)
        self.process_df()

    def process_df(self):
        self.df.Price.replace(r'\$', r'',
                              regex=True, inplace=True)
        self.df.Price.replace(r',', r'',
                              regex=True, inplace=True)
        self.df.Price = self.df.Price.astype(float)
        self.df.EditorsRating = self.df.EditorsRating.astype(float)
        self.df = self.df.loc[:, ~self.df.columns.str.contains('^Unnamed')]

    def sort_and_filter_by(self, price, rating=None, laptops_nr=15):
        new_df = self.df[self.df['Price'] <= price]
        new_df.sort_values(by=['Price'], inplace=True)
        if rating is None:
            return new_df
        new_df = self.df[self.df['EditorsRating'] >= rating]
        new_df.sort_values(by=['Price'], inplace=True)
        return new_df.head(laptops_nr)
