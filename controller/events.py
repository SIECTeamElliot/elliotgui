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


class EventRegistry():
    def __init__(self):
        self.events = [
            Event('up'),
            Event('down'),
            Event('left'),
            Event('right'),
            Event('kb_up'),
            Event('kb_down'),
            Event('kb_left'),
            Event('kb_right'),
        ]
        self.event_dict = {
            ev.event_key: ev for ev in self.events
        }
