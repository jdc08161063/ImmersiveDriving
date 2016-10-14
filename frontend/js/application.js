

function setSongs(songs) {
  var songlist = document.getElementById("songlist");
  var songsHtml = songs.toHTML();
  songlist.innerHTML = songsHtml;
}

var imageLink = "https://lh3.googleusercontent.com/-XIBDmNIb4xo/AAAAAAAAAAI/AAAAAAAAAEk/IIRqdHKj_8M/s0-c-k-no-ns/photo.jpg";

$(document).ready(function() {
  var song = new Song("ag", "gds", "gdf", imageLink);
  var songs = new Songlist([song, song, song, song]);
  setSongs(songs);
});
