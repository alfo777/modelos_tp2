from Garment import *
from WashingGroup import *


class GarmentManager:

    def __init__(self):
        self.garments = {}
        self.garmentsDict = {}
        self.garmentsDictAux = {}
        self.groups = []


    def createGarments(self):        
        firstProblemFile = open('segundo_problema.txt','r')
        lines = firstProblemFile.readlines()
        firstProblemFile.close()

        for line in lines[::-1]:
            if line.startswith("n"):
                n, nGarment, washTime = line.split(" ")
                self.garmentsDict[int(nGarment)] = Garment(int(nGarment), int(washTime))
            
            elif line.startswith("e"):
                e, nGarment, nGarmentIncampatible = line.split(" ")
                self.garmentsDict[int(nGarment)].addIncompatibleGarment(int(nGarmentIncampatible))



    def sortGarments(self):
        newList = []
        self.garments=sorted(self.garmentsDict.items(), key=lambda x: x[1].washTime, reverse=False)
        for g in self.garments:
            newList.append(g[1])

        self.garments = newList
        self.garmentsDictAux = self.garmentsDict.copy()
    


    def groupGarments(self):
        self.groups = []
        i = 0
        while( len(self.garments) != 0 ):       
            i += 1
            newGroup = self.createGroup(i)      
            self.groups.append(newGroup)

        self.getTotalTime()
                


    def createGroup(self, nro):
        group = WashingGroup(nro,self.garmentsDict,self.garmentsDictAux)
        firstGarment = self.garments[-1]
        group.addGament(firstGarment)

        addedGarments = group.addGarments()
        for g in addedGarments:
            self.garments.remove(g)
            
        return group



    def createSolutionFile(self):
        resultFile = open('solucion.txt','w')
        lines = []
        for group in self.groups:
            lines.extend(group.getGarments())

        lines.sort()
        
        for line in lines:
            resultFile.write("{} {}\n".format(line[0],line[1]))

        resultFile.close()


    def getTotalTime(self):
        time = 0
        isOk = True
        for aGroup in self.groups:
            time += aGroup.getTotalTime()
            
        print("tiempo total:", time)
        
    def washClothes(self):
        self.createGarments()
        self.sortGarments()
        self.groupGarments()
        self.createSolutionFile()
        



def main():
    g = GarmentManager()
    g.washClothes()


main()