
class Garment:

    def __init__(self, nroGarment,aTime):
        self.nro = nroGarment
        self.washTime = aTime
        self.incompatibleGarments = []


    def addIncompatibleGarment(self,nroGarment):
        self.incompatibleGarments.append(nroGarment)

    
    def isIncompatible(self, garment):
        return ( garment.nro in self.incompatibleGarments )


