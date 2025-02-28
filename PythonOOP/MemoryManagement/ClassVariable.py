class Sample():
    nObjects = 0

    def __init__(self, name):
        self.name = name
        Sample.nObjects += 1

    def howManyObjects(self):
        print('There are ', Sample.nObjects, ' objects')

    def __del__(self):
        Sample.nObjects -= 1

oSample1 = Sample('Object 1')
oSample2 = Sample('Object 2')
oSample3 = Sample('Object 3')
oSample4 = Sample('Object 4')

del oSample3

oSample1.howManyObjects()
