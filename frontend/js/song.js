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
    return '<md-list-item class="md-3-line md-long-text" layout="row" layout-padding>' +
        '<img ng-src=="' + this.cover + '?25" alt="" class="md-avatar" flex="20" flex-offset="20">' +
        '<div class="md-list-item-text" flex>' +
        '<h3 class="title">' + this.name + '</h3>' +
        '<p>' + this.artist + '<br>' + this.album + '</p>' +
        '<a href="#!" class="secondary-content"></a>' +
        '</div>' +
        '<md-divider></md-divider>' +
        '</md-list-item>';
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
