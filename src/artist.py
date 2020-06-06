# Import modules 

import pandas as pd
from ast import literal_eval
import json
from spotify import Spotify

class Artist(Spotify):
    def __init__(self):
        self.load_data()
        self.cast_to_list()

    def load_data(self, filename="data/data_w_genres.csv"):
        self.data = pd.read_csv(filename)

    def cast_to_list(self):
        self.data['genres'] = self.data.genres.apply(lambda x: literal_eval(x))

    def check_for_item(self, x, item='rap'):
        for i in x:
            if item in i:
                 return True
        return False

    def sort_by_popularity(self, filtered_data):
        return filtered_data.sort_values('popularity', ascending=False)
    
    def to_json(self, sorted_data):
        return json.loads(sorted_data.to_json(orient='records'))

    def artists_by_genre(self, genre):
        return self.to_json(self.sort_by_popularity(self.data[self.data.genres.apply(self.check_for_item, item=genre)]))
