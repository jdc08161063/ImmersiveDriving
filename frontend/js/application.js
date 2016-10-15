var _songs = null;
var _current_image = null;

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

function uploadImage(e) {
  var request = new Request(_current_image);
  request.perform(function(songs) {
    _songs = songs;
    updateSongsUI();
  });
   $('#image').attr('src', e.target.result);
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
                _current_image = this.files[0].name;
                var reader = new FileReader();
                reader.onload = uploadImage;
                reader.readAsDataURL(this.files[0]);
            }
        });
    });
