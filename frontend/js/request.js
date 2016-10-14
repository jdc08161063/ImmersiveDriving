var url = "http://localhost:5000";

var Request = function (imageName) {
    this.imageName = imageName;
};

Request.prototype.perform = function (callback) {
    $.get(url + "/" + this.imageName,
        function (data) {
            im = this.imageName
            callback(new Songlist(data[im]))
        });
};
