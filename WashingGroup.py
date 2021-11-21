

class WashingGroup:
    
    def __init__(self, id, garmentsDict, garmentsDictAux):
        self.garments = []
        self.id = id
        self.dict = garmentsDict
        self.auxDict = garmentsDictAux
        self.allowed = set()
        self.garmentsInGroup = set()

    
    def addGament(self, newGament):
        self.garments.append(newGament)
        del self.dict[newGament.nro]
        self.garmentsInGroup.add(newGament.nro)
        self.remainingGaments = set(self.dict.keys())
        self.allowed = self.allowed.union(self.remainingGaments.difference(newGament.incompatibleGarments))
    
    
    def addGarments(self):
        
        self.checkGarmentsLeft()
       
        return self.garments             


    def checkGarmentsLeft(self):
        goOn = True
        while goOn:
            nroBetterGament = -1
            maxTime = -1
            
            for nro in self.allowed:

                if nro in self.garmentsInGroup:
                    continue
                    
                elif self.canEnter(nro):
                    if self.dict[nro].washTime > maxTime:
                        maxTime = self.dict[nro].washTime
                        nroBetterGament = nro

                    elif self.dict[nro].washTime == maxTime and self.isBetterOption(nro,nroBetterGament):
                        nroBetterGament = nro

            if nroBetterGament == -1:
                goOn = False
            
            else:
                self.addGament(self.dict[nroBetterGament])


    def isBetterOption(self, nro, actualNro):
        
        actualIncompatibilities = set()
        newIncompatibilities = set()
        incompatibilities = set()
        actualTime = 0
        newTime = 0

        for i in self.garmentsInGroup:
            if i != nro and i != actualNro:
                incompatibilities = incompatibilities.union(self.auxDict[i].incompatibleGarments)

        actualIncompatibilities = incompatibilities.union(self.auxDict[actualNro].incompatibleGarments)
        newIncompatibilities = incompatibilities.union(self.auxDict[nro].incompatibleGarments)

        if len(newIncompatibilities) < len(actualIncompatibilities):
            return True

        for i in newIncompatibilities:
            newTime += self.auxDict[i].washTime
        
        for i in actualIncompatibilities:
            actualTime += self.auxDict[i].washTime

        return (newTime > actualTime)
    


    def canEnter(self, nro):
        for garment in self.garments:
            if self.areImcompatibles(garment,self.dict[nro]):
                return False
        
        return True


    def areImcompatibles(self,aGarment, anotherGarment):
        return (aGarment.isIncompatible(anotherGarment) or anotherGarment.isIncompatible(aGarment))
    

    def getTotalTime(self):
        time = 0
        for aGarment in self.garments:
            if time < aGarment.washTime:
                time = aGarment.washTime
        
        return time

    
    def getGarments(self):
        r = []
        for g in self.garments:
            r.append([g.nro, self.id])

        return r
            
                        



