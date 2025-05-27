class Song:
    def __init__(self, name, artist, category):
        self.name = name
        self.artist = artist
        self.category = category


    def __str__(self):
        return f"Трек {self.name} от {self.artist}! Жанр: {self.category}"



class SongSong:
    def __init__(self, name):
        self.name = name
        self.playlist = []


    def add_song(self, song):
        self.playlist.append(song)

    def show_all_songs(self):
        print(f"All songs in playlist {self.name}")
        if not self.playlist:
            print("No songs found")
        for song in self.playlist:
            print(f" - {song}")


    def delete_song(self, name):
        for song in self.playlist:
            if song.name.lower() == name.lower():
                self.playlist.remove(song)
                print(f"Deleted: {song}")
                return
        print("Song not found")






def main():
    playlist = SongSong("Playlist")


    while True:
        print("\n ===== PLAYLIST =====")
        print("1. Add song to playlist")
        print("2. Show all songs in playlist")
        print("3. Delete Song")
        print("4. Exit")
        choice = input("Choose an option (1-4)")


        if choice == "1":
            name = input("Song name: ")
            artist = input("Artist name: ")
            category = input("Category: ")
            song = Song(name, artist, category)
            playlist.add_song(song)

        elif choice == "2":
            playlist.show_all_songs()

        elif choice == "3":
            name = input("Enter the name of the track to delete: ")
            playlist.delete_song(name)

        elif choice == "4":
            print("See you son!")
            break

if __name__ == "__main__":
    main()

