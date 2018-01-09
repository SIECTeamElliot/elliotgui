import logging
from logging.handlers import RotatingFileHandler

class Event():
    def __init__(self, event_key, callback_trig_on=None, callback_trig_off=None, has_value=False, default_val=0):
        if has_value:
            self.value = default_val
        self.has_value = has_value
        self.enable = False
        self.event_key = event_key
        self.callback_trig_on = callback_trig_on
        self.callback_trig_off = callback_trig_off

    def trig_on(self):
        self.enable = True
        if callable(self.callback_trig_on):
            self.callback_trig_on()

    def trig_off(self):
        self.enable = False
        if callable(self.callback_trig_off):
            self.callback_trig_off()

class Callback:
    def __init__(self, event, logger):
        self.event = event
        self.logger = logger

    def __call__(self):
        print(self.event)
        self.logger.info(self.event)

class EventRegistry():
    def __init__(self, filename="./communication_file.txt"):
        self.handler = RotatingFileHandler(filename, mode='a', maxBytes=4*10 , backupCount=0, encoding=None, delay=0)
        self.handler.setLevel(logging.INFO)

        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)
        self.log.addHandler(self.handler)

        self.events = [
            Event('up', Callback('up', self.log)),
            Event('down', Callback('down', self.log)),
            Event('left', Callback('left', self.log)),
            Event('right', Callback('right', self.log)),
            Event('stop', Callback('stop', self.log)),
        ]
        self.event_dict = {
            ev.event_key: ev for ev in self.events
        }
