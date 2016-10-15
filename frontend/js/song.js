var Song = function (artist, name, album, cover, url) {
    this.artist = artist;
    this.name = name;
    this.album = album;
    this.cover = cover;
    this.playing = false;
    this.url = url;
    this.audio = null;
};

Song.prototype.toHTML = function (index) {
    return '<li class="collection-item avatar">' +
        '<img src="' + this.cover + '" alt="" class="circle">' +
        '<span class="title">' + this.name + '</span>' +
        '<p>' + this.artist + '<br>' + this.album + '</p>' +
        '<a href="#!" class="secondary-content"></a>' +
        '</li>';
};

Song.prototype.play = function () {
    this.audio = new SongPlayer(this.url);
    this.audio.fadeIn();
    this.playing = true;
};

Song.prototype.pause = function () {
    this.playing = false;
    if (this.audio)
        this.audio.fadeOut();
};
