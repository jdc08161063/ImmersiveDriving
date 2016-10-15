var SongPlayer = function (src) {
    this.src = src;
    this.id=0;
    this.sound = new Howl({
        src: [src]
    });
};

SongPlayer.prototype.fadeIn = function() {
    this.id = this.sound.play();
    this.sound.fade(0.1,1,this.sound.duration()/2,this.id);
};

SongPlayer.prototype.fadeOut = function() {
    this.sound.fade(0.9,0,this.sound.duration()/2,this.id);
};