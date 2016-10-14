var Songlist = function(songs) {
  this.songs = songs;
};

Songlist.prototype.toHTML = function () {
  var songsHtml = this.songs.reduce(function(acc, song) {
    return acc + song.toHTML();
  }, '');
  return '<ul class="collection">' + songsHtml + '</ul>';
};
