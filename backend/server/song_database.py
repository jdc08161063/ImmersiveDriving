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
    "city_street_urban": [Song("Bomfunk MC", "Freestyler", "-", "-",
                               "http://www.youtube.com/watch?v=ymNFyxvldaM"),
                          Song("Eminem", "Lose yourself", "Lose yourself", "-",
                               "http://www.youtube.com/watch?v=eRhEcKHU5LY"),
                          Song("Linkin Park", "Numb", "Meteora", "-",
                               "http://www.youtube.com/watch?v=kXYiU_JCYtU"),
                          ],
    "desert_field_void": [],
    "forest_mountain_nature": [],
    "night_tunnel_dark": [],
    "sea_coast_water": [Song("Movie theme", "Pirates of the Carribean", "-", "-",
                             "http://www.youtube.com/watch?v=27mB8verLK8"),
                        Song("Movie theme", "Pirates of the Carribean", "-", "-",
                             "http://www.youtube.com/watch?v=27mB8verLK8"),
                        ],
    "surprise_unknown": [],
    "road_highway_boredom": [],
}
