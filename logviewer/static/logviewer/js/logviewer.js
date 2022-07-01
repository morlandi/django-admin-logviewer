
class Log {

    constructor(element, log_id, path) {
        this.element = element;
        this.log_id = log_id;
        this.path = path;
        this.last_position = 0;
        this.current_scroll_position = 0;
        this.timer = null;
    }

    update() {
        var self = this;
        var visible = this.element.is(':visible');

        if (visible) {
            self.getLines();
        }
        else {
            if (self.last_position > 0) {
                self.last_position = 0;
                self.element.text('');
            }
        }

        self.start();
    }

    start() {
        var self = this;
        self.timer = window.setTimeout(function() {self.update();}, REFRESH_INTERVAL);
    }

    // stop() {
    //     var self = this;
    //     window.clearTimeout(self.timer);
    // }

    getLines() {
        var self = this;
        var url = LOGVIEWER_URL_GETLOGLINES.replace("11111", self.log_id);
        self.current_scroll_position = self.element.scrollTop();

        $.ajax({
            url: url,
            type: "get",
            data: {
                last_position: self.last_position,
            },
            success: function(result) {
                console.log('new lines: %o', result.content.length);
                self.last_position = result.last_position;
                self.printLines(result.content);
            },
            dataType: "json"
        });

    }

    printLines(lines) {
        var self = this;

        for (var i=0; i<lines.length; i++) {
            if (lines[i].length > 0) {
                self.element.append(lines[i]);
            }
        }

        var autoscroll = $('#scroll-' + self.log_id).prop('checked');
        if (autoscroll && lines.length) {
            self.element.scrollTop(self.element[0].scrollHeight - self.element.height());
        }
        else {
            self.element.scrollTop(self.current_scroll_position);
        }

    }

}

