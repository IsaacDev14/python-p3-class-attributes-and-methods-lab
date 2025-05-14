class Song:
    #class attributes
    count = 0
    genres = []
    artists = []
    genre_count  =[]
    artist_count = []

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

    #update class-level data
    self.add_song_to_count()
    self.add_song_to_genres(genre)
    self.add_to_artists(artist)
    self.add_to_genre_count(genre)
    self.add_to_artist_count(artist)

