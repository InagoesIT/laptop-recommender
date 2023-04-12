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

    def sort_and_filter_by(self, price, rating=None, laptops_nr=5):
        new_df = self.df[self.df['Price'] <= price].copy()
        filter_by = ['Price']
        if rating is not None:
            filter_by.append('EditorsRating')
            new_df = new_df[new_df['EditorsRating'] >= rating].copy()
        new_df.sort_values(by=filter_by, inplace=True)
        return new_df.head(laptops_nr)
