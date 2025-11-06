import pandas as pd
import numpy as np

class EnergyDataProcessor:
    def __init__(self, file_path: str):
        self.df = pd.read_csv(file_path)
        self.clean_data()

    def clean_data(self):
        self.df['date'] = pd.to_datetime(self.df['date'])
        self.df['year'] = self.df['date'].dt.year
        self.df['month'] = self.df['date'].dt.month
        self.df['day'] = self.df['date'].dt.day
        self.df['hour'] = self.df['date'].dt.hour
        self.df['weekday'] = self.df['date'].dt.day_name()
        self.df['fotovolt'] = self.df['fotovolt'].apply(lambda x: np.nan if x < 0 else x)
        self.df['fotovolt'] = self.df['fotovolt'].fillna(0)
        self.df = self.df.drop_duplicates()

        return self.df

    def descriptive_stats(self):
        return self.df.describe().T