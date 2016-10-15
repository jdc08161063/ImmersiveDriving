import json


class Song(object):
    def __init__(self, artist, name, album, cover, url):
        super(Song, self).__init__()
        self.artist = artist
        self.name = name
        self.album = album
        self.cover = cover
        self.url = url

    def to_json(self):
        return json.dumps(self.__dict__)

songs_map = {
    "city_street_urban": [Song("Abba", "Summer Night City", "-", "http://img.youtube.com/vi/_d5dPYHi17k/0.jpg",
                               "../backend/server/songs/cityStreetUrban/summer_night_city.mp3"),
                          ],
    "desert_field_void": [],
    "forest_mountain_nature": [Song("David Garrett", "Human Nature", "-", "http://img.youtube.com/vi/4RTP1JWn6ZM/0.jpg",
                               "../backend/server/songs/forestMountainNature/human_nature.mp3")],
    "night_tunnel_dark": [Song("Adele", "Love in the Dark", "-", "http://img.youtube.com/vi/97hZ4bxTqZc/0.jpg",
                               "../backend/server/songs/nightTunnelDark/love_in_the_dark.mp3")],
    "sea_coast_water": [Song("Movie theme", "Pirates of the Carribean", "-", "http://img.youtube.com/vi/27mB8verLK8/hqdefault.jpg",
                             "../backend/server/songs/sample_song.mp3")
                        ],
    "surprise_unknown": [Song("-", "Ans Ende Der Welt", "-", "",
                             "../backend/server/songs/surprise/ans_ende_der_welt.mp3")],
    "road_highway_boredom": [Song("Hermes House Band", "Country Roads", "-", "http://img.youtube.com/vi/ZVz_IJoyO6Y/0.jpg",
                             "../backend/server/songs/roadHighway/country_roads.mp3"],
}
