# Import modules 

import pandas as pd
from ast import literal_eval
import json

class Genre():
    def __init__(self):
        self.load_data()
        self.sort_by_popularity()

    def load_data(self, filename="../data/data_by_genres.csv"):
        self.data = pd.read_csv(filename)

    def sort_by_popularity(self):
        self.data.sort_values('popularity', ascending=False, inplace=True)
    
    def to_json(self, sorted_data):
        return json.loads(sorted_data.to_json(orient='records'))

    def popular_genres(self):
        return self.to_json(self.data)
