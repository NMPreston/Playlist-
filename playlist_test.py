# Noah Preston, CSC-231-001

from playlist import Song, Playlist

song1 = Song("Blind", "Korn", "Korn", False, 258, "Metal")
song2 = Song("Photograph", "Pyromania", "Def Leppard", True, 248, "Rock")
song3 = Song("How to Fly", "Caress Your Soul", "Sticky Fingers", False, 202, "Alternative")

print("String method:")
print(song1)
print(song2)

print("\nEqual method:")
print(f"song1 == song2: {song1 == song2}")  
print(f"song1 == song1: {song1 == song1}")

print("\nPlay method:")
song1.play()  
print(f"Song 1 plays: {song1.plays}")  

print("\nGet and Set duration:")
print(f"Original duration: {song1.get_duration()} seconds")
song1.set_duration(300)
print(f"Updated duration: {song1.get_duration()} seconds")

print("\nPlaylist:")
playlist = Playlist([song1, song2])
print(f"Initial playlist duration: {playlist.duration} seconds")

print("\nAdding a song to the playlist:")
playlist = playlist + song3  
print(f"Updated playlist duration: {playlist.duration} seconds")

print("\nSongs in the playlist:")
for song in playlist.songs:
    print(song)
