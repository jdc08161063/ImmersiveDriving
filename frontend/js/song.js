var Song = function(artist, name, album, albumCover) {
  this.artist = artist;
  this.name = name;
  this.album = album;
  this.albumCover = albumCover;
};

Song.prototype.toHTML = function () {
  return '<li class="collection-item avatar"><img src="' + this.albumCover + '" alt="" class="circle"><span class="title">' + this.name + '</span><p>' + this.artist + '<br>' + this.album + '</p><a href="#!" class="secondary-content"><i class="material-icons">grade</i></a></li>';
};
