class Card(object):
    """
    Fields:
    _name
    _atk
    _def
    _ready

    Methods:
    __init__
    __str__
    Getters for _name, _atk, _def & _ready
    update_ready

    """

    def __init__(self, name, attack, defence):
        self._name = name
        self._atk = attack
        self._def = defence
        self._ready = 0


    def __str__(self):
        output = self._name +', '+str(self._atk)+', '+str(self._def)
        return output


    #Make sure this is only called when ready is less than 2
    def update_ready(self, position_on_field):
        if position_on_field == 5:
            self.ready += 1
        else:
            self.ready = 2


    #Getters
    @property
    def name(self):
        return self._name

    
    @property    
    def attack(self):
        return self._atk


    @property
    def defence(self):
        return self._def


    @property
    def ready(self):
        return self._ready

def import_test():
    print('Module successfully imported')
