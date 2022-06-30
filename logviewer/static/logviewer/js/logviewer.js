
class Log {

    constructor(element, path) {
        this.element = element;
        this.path = path;

        this.timer = null;
        this.timeout = 2000;
        this.scroll = true;
        this.first_read = true;

    }

    startReading() {
        var self = this;
        if (self.first_read) {
            console.log('first %o', self.path);
            self.first_read = false;
        }
        else {
            console.log('next %o', self.path);
        }
        self.timer = window.setTimeout(function() {self.getLines();}, self.timeout);
    }

    getLines() {
        var self = this;
        console.log('getLines(), %o', self.path);
        self.printLines();
    }

    printLines() {
        var self = this;
        console.log('printLines(), %o', self.path);
        self.timer = window.setTimeout(function() {self.getLines();}, self.timeout);
    }

}

