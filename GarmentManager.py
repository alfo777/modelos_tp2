from Garment import *
from WashingGroup import *


class GarmentManager:

    def __init__(self):
        self.garments = {}
        self.groups = []


    def createGarments(self):        
        firstProblemFile = open('segundo_problema.txt','r')
        lines = firstProblemFile.readlines()
        firstProblemFile.close()

        for line in lines[::-1]:
            if line.startswith("n"):
                n, nGarment, washTime = line.split(" ")
                self.garments[int(nGarment)] = Garment(int(nGarment), int(washTime))
            
            elif line.startswith("e"):
                e, nGarment, nGarmentIncampatible = line.split(" ")
                self.garments[int(nGarment)].addIncompatibleGarment(int(nGarmentIncampatible))



    def sortGarments(self):
        newList = []
        self.garments=sorted(self.garments.items(), key=lambda x: x[1].washTime, reverse=False)
        for g in self.garments:
            newList.append(g[1])

        self.garments = newList
    


    def groupGarments(self):
        self.groups = []
        i = 0
        while( len(self.garments) != 0 ):       
            i += 1
            newGroup = self.createGroup(i)      
            self.groups.append(newGroup)
                

    def createGroup(self, nro):
        group = WashingGroup(nro)
        pushOuts = []

        for garment in self.garments[::-1]:
            pushOuts, result = group.addGament(garment)

            if result:
                self.garments.remove(garment)
                            
            self.garments.extend(pushOuts)
        
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

        
    def washClothes(self):
        self.createGarments()
        self.sortGarments()
        self.groupGarments()
        self.createSolutionFile()
        



def main():
    g = GarmentManager()
    g.washClothes()


main()