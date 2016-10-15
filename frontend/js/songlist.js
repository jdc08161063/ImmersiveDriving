var Songlist = function(songs) {
  this.songs = songs;
  if (songs.length != 0) {
    this.songs[0].play();
  }
};

Songlist.prototype.toHTML = function () {
  var songsHtml = this.songs.reduce(function(acc, song, index) {
    return acc + song.toHTML(index);
  }, '');
  return '<md-list flex="100" layout="column" class="song-list" layout-wrap>' + songsHtml + '</md-list>';
};

Songlist.prototype.play = function (index) {
    for (var i in this.songs) {
      this.songs[i].pause();
    }
    this.songs[index].play();
};

Songlist.prototype.pause = function () {
    songs.forEach(function(song) {
        if (song.playing) {
            song.pause()
        }
    })
};
