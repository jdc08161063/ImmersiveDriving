var _songs = null;

function updateSongsUI() {
    var songlist = document.getElementById("songlist");
    songlist.innerHTML = _songs.toHTML();
}

function play(index) {
    _songs.play(index);
    updateSongsUI();
}

function getNextImage() {
    if (_songs != null) {
        _songs.pause();
    }
    var request = new Request();
    request.perform(function (songs, imageName, label) {
        _songs = songs;
        $('#image').css('background-image', "url(images/" + imageName + ")");
        document.getElementById("label").innerHTML = label;
        updateSongsUI();
    });
}

$(document).ready(function () {
    getNextImage();
});

angular.module('ImmersiveDriving', ['ngAnimate',
    'ngAria',
    'ngMaterial']);
