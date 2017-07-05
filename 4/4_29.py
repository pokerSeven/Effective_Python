

class Resistor(object):
    def __init__(self,ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0

class VoltageResistance(Resistor):
    def __init__(self,ohms):
        Resistor.__init__(ohms)
        self._voltage = 0

@property
def voltage(self):
    return self._voltage

@voltage.setter
def voltage(self,voltage):
    self._voltage = voltage
    self.current= self._voltage / self.ohms
