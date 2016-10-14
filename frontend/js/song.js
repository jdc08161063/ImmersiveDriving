var Song = function(artist, name, album, albumCover, url) {
  this.artist = artist;
  this.name = name;
  this.album = album;
  this.albumCover = albumCover;
  this.playing = false;
  this.url = url;
  this.audio = null;
};

Song.prototype.toHTML = function (index) {
  return '<li class="collection-item avatar"><img src="' + this.albumCover + '" alt="" class="circle"><span class="title">' + this.name + '</span><p>' + this.artist + '<br>' + this.album + '</p><a href="#!" class="secondary-content"><i class="material-icons" onClick="play(' + index + ')">' + (this.playing ? 'pause' : 'play_arrow') + '</i></a></li>';
};

Song.prototype.play = function () {
  this.audio = new Audio(this.url);
  this.audio.play();
  this.playing = true;
};

Song.prototype.pause = function () {
  this.playing = false;
  if (this.audio)
    this.audio.pause();
};
