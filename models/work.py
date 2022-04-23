class Work:
    def __init__(self, title, artist, year, museum, id = None):
        self.title = title
        self.artist = artist
        self.year = year
        self.museum = museum
        self.id = id

    def get_details(self):
        return f"{self.title} by {self.artist} is in {self.museum.name}"
