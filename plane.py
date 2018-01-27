class Plane(object):
    def __init__(self, initial_status='flying'):
        self.status = initial_status

    def land(self):
        self.status = 'landed'
