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
    "city_street_urban": [
        Song("Imagine Dragons", "Amsterdam", "-", "https://i.ytimg.com/vi/TKtPXO5iEnA/maxresdefault.jpg",
             "../backend/server/songs/cityStreetUrban/amsterdam.m4a"),
        Song("Abba", "Summer Night City", "-", "http://img.youtube.com/vi/_d5dPYHi17k/0.jpg",
             "../backend/server/songs/cityStreetUrban/summer_night_city.mp3"),
    ],
    "field_plains": [
        Song("Lukas Graham", "7 Years", "-", "http://img.youtube.com/vi/LHCob76kigA/0.jpg",
             "../backend/server/songs/desertFieldVoid/7years.m4a"),
        Song("Olly Murs", "Right Place Right Time", "-", "http://img.youtube.com/vi/8lxaNO5V06k/0.jpg",
             "../backend/server/songs/desertFieldVoid/right_place_right_time.m4a")],
    "forest_mountain_nature": [
        Song("David Garrett", "Human Nature", "-", "http://img.youtube.com/vi/4RTP1JWn6ZM/0.jpg",
             "../backend/server/songs/forestMountainNature/human_nature.mp3")],
    "night_tunnel_dark": [
        Song("Adele", "Love in the Dark", "-", "http://img.youtube.com/vi/97hZ4bxTqZc/0.jpg",
             "../backend/server/songs/nightTunnelDark/love_in_the_dark.mp3"),
        Song("Adele", "Skyfall", "-", "http://img.youtube.com/vi/DeumyOzKqgI/0.jpg",
             "../backend/server/songs/nightTunnelDark/skyfall.m4a"),
        Song("Imagine Dragons", "Every Night", "-", "http://img.youtube.com/vi/kuijhOvKyYg/0.jpg",
             "../backend/server/songs/nightTunnelDark/every_night.m4a"),
        Song("Coldplay", "A Sky Full of Stars", "-", "http://img.youtube.com/vi/97hZ4bxTqZc/0.jpg",
             "../backend/server/songs/nightTunnelDark/a_sky_full_of_stars.m4a")
    ],
    "sea_coast_water": [
        Song("Coldplay", "Every Teardrop is a Waterfall", "-", "http://img.youtube.com/vi/fyMhvkC3A84/0.jpg",
             "../backend/server/songs/seaCoastWater/every_teardrop_is_a_waterfall.mp3"),
        Song("Movie theme", "Pirates of the Carribean", "-", "http://img.youtube.com/vi/27mB8verLK8/hqdefault.jpg",
             "../backend/server/songs/sample_song.mp3")
    ],
    "surprise_unknown": [
        Song("Wiz Khalifa", "See You Again", "-", "http://img.youtube.com/vi/RgKAFK5djSk/0.jpg",
             "../backend/server/songs/surprise/see_you_again.m4a"),
        Song("-", "Ans Ende Der Welt", "-", "",
             "../backend/server/songs/surprise/ans_ende_der_welt.mp3")],
    "road_highway_boredom": [
        Song("Hermes House Band", "Country Roads", "-", "http://img.youtube.com/vi/ZVz_IJoyO6Y/0.jpg",
             "../backend/server/songs/roadHighway/country_roads.mp3"),
        Song("Lena", "Wild And Free", "-", "",
             "../backend/server/songs/roadHighway/wild_and_free.m4a")]
}
