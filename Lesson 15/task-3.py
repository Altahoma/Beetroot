CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.amount = len(channels)
        self.current = 0

    def is_exist(self, channel):
        return 'Yes' if channel in self.channels or 1 <= channel <= self.amount else 'No'

    def first_channel(self):
        self.current = 0
        return self.channels[self.current]

    def last_channel(self):
        self.current = self.amount - 1
        return self.channels[self.current]

    def turn_channel(self, channel):
        if self.is_exist(channel) == 'Yes':
            self.current = channel-1
            return self.channels[self.current]

    def next_channel(self):
        if self.current + 1 == self.amount:
            self.current = 0
        else:
            self.current += 1
        return self.channels[self.current]

    def previous_channel(self):
        if self.current == 0:
            self.current = self.amount - 1
        else:
            self.current -= 1
        return self.channels[self.current]

    def current_channel(self):
        return self.channels[self.current]


controller = TVController(CHANNELS)

assert controller.first_channel() == "BBC"
assert controller.last_channel() == "TV1000"
assert controller.turn_channel(1) == "BBC"
assert controller.next_channel() == "Discovery"
assert controller.previous_channel() == "BBC"
assert controller.current_channel() == "BBC"
assert controller.is_exist(4) == "No"
assert controller.is_exist("BBC") == "Yes"
