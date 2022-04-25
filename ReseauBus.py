from Ligne import *
from Stop import *
from sys import *

nbArcsMini=1000


def min(old,new):
    if new==None or new>old:
        return old
    else :
        return new

class ReseauBus:
    def __init__(self,lignes):
        self.lignes=lignes

    def findStops(self,stop): #renvoie une liste des lignes comprenant l'arrret stop
        res=[]
        for e in self.lignes:
            if e.isHere(stop):
                res.append(e)
        return res

    def findTheStop(self,stop):
        for e in self.lignes:
            if e.findStop(stop)!=None:
                return e.findStop(stop)
        return None


    def shortest(self,start,end):
        startingStop=self.findTheStop(start)
        endingStop=self.findTheStop(end)
        def shortestbis(self,nbArcs,stop,end):
            print(stop)
            if stop==end:
                return nbArcs
            else:
                for i in range(len(self.findStops(stop))):
                    ligne=self.findStops(stop)[i]
                    print(ligne)
                    print(i)
                    if stop.get_next_stop(ligne)==None:
                        print("terminus")
                    else:
                        return shortestbis(self,nbArcs+1,stop.get_next_stop(ligne),end)
   
        return shortestbis(self,0,startingStop,endingStop)
                

    def shortestDijkstra(self,start,end):
        listNoeudsAVisiter = self.getAllStope()
        listPlusCoursChemin = self.genInitialPlusCoursChemin() #dictionare où les clefs sont les stops et les valeur sont l'infini

        listNoeudsAVisiter.remove(start)
        listPlusCoursChemin[start] = 0

        def shortestDijkstra_sub(self, current, end, listNoeudsAVisiter, listPlusCoursChemin):
            if(current == end):
                return listPlusCoursChemin
            listPlusCoursChemin = miseAjourDistance(current, listPlusCoursChemin)
            nouveauCurrent = getNewCurrent(listNoeudsAVisiter, listPlusCoursChemin)
            listNoeudsAVisiter.remove(nouveauCurrent)
            return self.shortestDijkstra_sub(nouveauCurrent, end, listNoeudsAVisiter, listPlusCoursChemin)

        return self.shortestDijkstra_sub(current, end, listNoeudsAVisiter, listPlusCoursChemin)
