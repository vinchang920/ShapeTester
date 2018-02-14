    
class Sphere(object):
    vol = 0
    SA = 0
    radius = 0
    pi= 3.14

    def __init__(self):
        self.radius = 0

    def volume(self):
        vol = (4/3)*3.14*(self.radius**3)
        vol = self.radius
    def SA(self):
        SA = 4*3.14*self.radius**25
