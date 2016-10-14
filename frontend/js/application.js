var _songs = null;

function updateSongsUI() {
  var songlist = document.getElementById("songlist");
  var songsHtml = _songs.toHTML();
  songlist.innerHTML = songsHtml;
}

function play(index) {
  _songs.play(index);
  updateSongsUI();
}

function setSongs(songs) {
  _songs = songs;
  updateSongsUI();
}

function uploadImage(file) {
  var request = new Request(file.name);
  request.perform(function(songs) {
    _songs = songs;
    updateSongsUI();
  });
  var imageView = document.getElementById("image");
  imageView.src = image.target.result;
}

var imageLink = "https://lh3.googleusercontent.com/-XIBDmNIb4xo/AAAAAAAAAAI/AAAAAAAAAEk/IIRqdHKj_8M/s0-c-k-no-ns/photo.jpg";

$(document).ready(function() {
  var song = new Song("ag", "gds", "gdf", imageLink);
  var songTwo = new Song("fd", "fgd", "gfsd", imageLink);
  var songs = new Songlist([song, song, songTwo, song]);
  setSongs(songs);
});

$(function () {
        $(":file").change(function () {
            if (this.files && this.files[0]) {
                var reader = new FileReader();
                reader.onload = uploadImage;
                reader.readAsDataURL(this.files[0]);
            }
        });
    });
