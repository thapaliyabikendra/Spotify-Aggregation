# Import modules 

import pandas as pd
from ast import literal_eval
import json
from spotify import Spotify


class Song(Spotify):
    def __init__(self):
        self.load_data()
        self.cast_to_list()

    def load_data(self, filename="data/data.csv"):
        self.data = pd.read_csv(filename, parse_dates=['year'], index_col='year')

    def cast_to_list(self):
        self.data['artists'] = self.data.artists.apply(lambda x: literal_eval(x))

    def check_for_item(self, x, item='Eminem'):
        for i in x:
            if i == item:
                 return True
        return False

    def sort_by_popularity(self, filtered_data):
        return filtered_data.sort_values('popularity', ascending=False).reset_index(drop=True)
    
    def to_json(self, sorted_data):
        return json.loads(sorted_data.to_json(orient='records'))

    def songs_by_year(self, year):
        return self.to_json(self.sort_by_popularity(self.data[self.data.index.year == year]))

    def songs_by_artist(self, artist):
        return self.to_json(self.sort_by_popularity(self.data[self.data.artists.apply(self.check_for_item, item=artist)]))
