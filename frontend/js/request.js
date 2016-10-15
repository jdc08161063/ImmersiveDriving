var url = "http://localhost:5000";

var Request = function (imageName) {
    this.imageName = imageName;
};

Request.prototype.perform = function (callback) {
    console.log(url + "/" + this.imageName);
    im = this.imageName;
    $.ajax({
        url: url + "/" + this.imageName,
        type: "GET",
        data: '',
        success: function (data) {
            songsJSON = data[im];
            songs = songsJSON.map(function (songString) {
                songObj = JSON.parse(songString);
                return new Song(songObj.artist, songObj.name, songObj.album, songObj.cover, songObj.url);
            });
            console.log(songs);
            callback(new Songlist(songs));
        }
    });
};
