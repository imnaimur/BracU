class Spotify:
    def __init__(self,sL) -> None:
        self.song_list = sL
    # """sir i created a variable self.len =len(self.song_list)"""
    def playing_number(self,n):
        if len(self.song_list)<n:
            print(f"{n} number song not found. Your playlist has {len(self.song_list)} songs only.")
        else:
            print(f"Playing {n} number song for you ")
            print("Song name:",self.song_list[n-1])
        return "##########################"
    def add_to_playlist(self,itm):
        self.song_list.append(itm)
        # print(self.song_list)


user1 = Spotify(["See You Again", "Uptown Funk", "Hello"])
print("=========================")
print(user1.playing_number(4))
user1.add_to_playlist("Dusk Till Dawn")
print(user1.playing_number(3))
print(user1.playing_number(4))