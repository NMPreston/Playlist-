# Noah Preston, CSC-231-001

class Song:
    def __init__(self, title, album, artist, is_cover, duration, genre):
        self.title = title
        self.album = album
        self.artist = artist
        self.is_cover = is_cover
        if duration > 0:
            self.duration = duration
        else:
            raise ValueError("Value must be greater than 0")
        self.genre = genre
        self.plays = 0

    def __str__(self):
        return f"Title: {self.title}; Artist: {self.artist}; Duration: {self.duration}; Genre: {self.genre}; is_cover: {self.is_cover}"

    def __eq__(self, other):
        if not isinstance(other, Song):
            return False
        return (self.title == other.title and 
                self.album == other.album and 
                self.artist == other.artist and 
                self.is_cover == other.is_cover and
                self.duration == other.duration and 
                self.genre == other.genre)

    def play(self):
        print(f"Played: {self.title} by {self.artist}")
        self.plays += 1

    def get_duration(self):
        return self.duration

    def set_duration(self, value):
        if value > 0:
            self.duration = value
        else:
            raise ValueError("The duration must be greater than 0")
    

class Playlist:
    def __init__(self, songs):
        self.songs = songs
        self.duration = sum(song.duration for song in songs)

    def __add__(self, new_song):
        if new_song not in self.songs:
            self.songs.append(new_song)
            self.duration += new_song.duration
        return self



