class Data:
    def __init__(self, object=None):
        self.type = type(object).__name__
        if object is None:
            self.data = []
        else:
            self.data = object


class Settings:
    def __init__(self, leading_wave, pulses):
        self.leading_wave = leading_wave
        self.pulses = pulses
    

