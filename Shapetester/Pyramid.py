class Pyramid(object):
    vol = 0
    SA = 0
    slantHeight = 0
    altitude = 0
    base = 0

    def __init__(self):
        self.slantheight=0
        self.altitude = 0
        self.base = 0
    def volume(self):
        self.slantheight*self.altitude*self.base
    def SA(self):
        SA = ((self.base*self.slantHeight)/2)*4
