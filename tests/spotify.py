from abc import ABC, abstractmethod

class Spotify(ABC):

    @abstractmethod
    def load_data(self, filename):
        pass

    @abstractmethod
    def cast_to_list(self):
        pass

    @abstractmethod
    def check_for_item(self, x, item):
        pass

    @abstractmethod
    def sort_by_popularity(self, filtered_data):
        pass

    @abstractmethod
    def to_json(self, sorted_data):
        pass
