import pandas as pd

class DataModel:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = pd.read_csv(filepath, sep=';')

