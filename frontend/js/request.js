var url = "super-secret-url";

var Request = function(data) {
  this.data = data;
};

Request.prototype.perform = function(callback) {
  var request = new XMLHttpRequest();
  request.onreadystatechanged = function() {
    if (request.readyState === XMLHttpRequest.DONE && request.status === 200) {
      var songs = JSON.parse(request.responseText).map(function(item) {
        return new Song(item.artist, item.name, item.album, item.cover, item.url);
      });
      callback(new Songlist(songs));
    }
  };

  // TODO: attach image from data. Preferably using multiform data

  request.open("GET", url);
  request.send();
};
