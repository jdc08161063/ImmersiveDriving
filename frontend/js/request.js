var url = "http://localhost:5000";

var Request = function () {
};

Request.prototype.perform = function (callback) {
    console.log(url + "/next");
    $.ajax({
        url: url + "/next",
        type: "GET",
        data: '',
        success: function (data) {
            imageFile = data["imageFile"];
            songsJSON = data["songs"];
            label = data["label"];
            songs = songsJSON.map(function (songString) {
                songObj = JSON.parse(songString);
                return new Song(songObj.artist, songObj.name, songObj.album, songObj.cover, songObj.url);
            });
            console.log(songs);
            callback(new Songlist(songs), imageFile, label);
        }
    });
};
