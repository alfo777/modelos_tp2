

class WashingGroup:
    
    def __init__(self, id):
        self.garments = []
        self.id = id

    # "removes" contiene la lista de prendas que deben ser removidas del grupo
    #  para insertar una prenda con tiempo de lavado mas alto que todas ellas
    # hay que mencionar tambien que este metodo devuelve false si
    # la prenda a agregar no pudo ser insertada, y true si la prenda si pudo ser agregada
    # tambien devuelve la lista removes para que las prendas rechazadas vuelvan a ser evauluadas
    # mas tarde para poder formar parte de un grupo
    def addGament(self, newGarment):
        incompativilities = []
        removes = []
        for i in range(len(self.garments)):
            
            if ( self.areImcompatibles(self.garments[i],newGarment) and self.garments[i].washTime >= newGarment.washTime ):
                if self.garments[i].nro == 1 and newGarment.nro==17:
                    print("aqui 1")

                elif self.garments[i].nro == 17 and newGarment.nro==1:
                    print("aqui 2")

                return [], False

            elif ( self.areImcompatibles(self.garments[i],newGarment) and self.garments[i].washTime < newGarment.washTime ):
                if self.garments[i].nro == 1 and newGarment.nro==17:
                    print("aqui 3")

                elif self.garments[i].nro == 17 and newGarment.nro==1:
                    print("aqui 4")
                incompativilities.append(i)


        for i in incompativilities[::-1]:
            aGarment = self.garments.pop(i)
            removes.append(aGarment)

        self.garments.append(newGarment)

        return removes, True

    def areImcompatibles(self,aGarment, anotherGarment):
        return (aGarment.isIncompatible(anotherGarment) or anotherGarment.isIncompatible(aGarment))

    
    def getGarments(self):
        r = []
        for g in self.garments:
            r.append([g.nro, self.id])

        return r
            
                        



