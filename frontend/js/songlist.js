var Songlist = function(songs) {
  this.songs = songs;
  this.songs[0].play();
};

Songlist.prototype.toHTML = function () {
  var songsHtml = this.songs.reduce(function(acc, song, index) {
    return acc + song.toHTML(index);
  }, '');
  return '<ul class="collection">' + songsHtml + '</ul>';
};

Songlist.prototype.play = function (index) {
  if (this.songs[index].playing) {
    this.songs[index].pause();
  } else {
    for (var i in this.songs) {
      this.songs[i].pause();
    }
    this.songs[index].play();
  }
};
