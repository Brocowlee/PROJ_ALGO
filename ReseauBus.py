from asyncio.windows_events import NULL
from Ligne import *
from Stop import *
from sys import *
from math import inf

nbArcsMini=1000


def min(old,new):
    if new==None or new>old:
        return old
    else :
        return new

def majDicoDistance(current,dico):
    stops=current.get_next_stops()
    for s in stops:
        newDist=dico[current]+1
        if newDist<dico[s]:
            dico[s]=newDist
    return dico

def getNewCurrent(listAllStops,dicoShortest):
    nextCurrent=listAllStops[0]
    nextCurrentDist=dicoShortest[nextCurrent]
    for s in listAllStops:
        if dicoShortest[s]<nextCurrentDist:
            nextCurrent=s
            nextCurrentDist=dicoShortest[s]
    return nextCurrent

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

    def getAllStops(self):
        res=[]
        for e in self.lignes:
            stop=e.start
            while stop!=None:
                res.append(stop)
                stop=stop.get_next_stop(e)
        return res

    def initDicoShortest(self):
        res={}
        for e in self.getAllStops():
            res[e]=inf
        return res



    # def shortest(self,start,end):
    #     startingStop=self.findTheStop(start)
    #     endingStop=self.findTheStop(end)
    #     def shortestbis(self,nbArcs,stop,end):
    #         print(stop)
    #         if stop==end:
    #             return nbArcs
    #         else:
    #             for i in range(len(self.findStops(stop))):
    #                 ligne=self.findStops(stop)[i]
    #                 print(ligne)
    #                 print(i)
    #                 if stop.get_next_stop(ligne)==None:
    #                     print("terminus")
    #                 else:
    #                     return shortestbis(self,nbArcs+1,stop.get_next_stop(ligne),end)
   
    #     return shortestbis(self,0,startingStop,endingStop)
                

    def shortestDijkstra(self,start,end):
        startingStop=self.findTheStop(start)
        endingPoint=self.findTheStop(end)
        listAllStops=self.getAllStops()
        dicoShortest=self.initDicoShortest()
        listAllStops.remove(startingStop)
        dicoShortest[startingStop]=0
        def shortestBis(self,current,end,listAllStops,dicoShortest):
            if current==end:
                return dicoShortest
            dicoShortest=majDicoDistance(current,dicoShortest)
            newCurrent=getNewCurrent(listAllStops,dicoShortest)
            listAllStops.remove(newCurrent)
            return shortestBis(self,newCurrent,end,listAllStops,dicoShortest)
            
        return shortestBis(self,startingStop,endingPoint,listAllStops,dicoShortest)