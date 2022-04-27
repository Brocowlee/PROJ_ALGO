from asyncio.windows_events import NULL
from Ligne import *
from Stop import *
from sys import *
from math import inf
import copy

nbArcsMini=1000


def min(old,new):
    if new==None or new>old:
        return old
    else :
        return new

def majDicoArcs(current,dico):
    for s in current.next_stop:
        newDist=dico[current][0]+1
        if newDist<dico[s][0]:
            dico[s][0]=newDist
            dico[s][1]=current
    return dico


def getNewCurrent(listAllStops,dicoShortest):
    nextCurrent=listAllStops[0]
    nextCurrentDist=dicoShortest[nextCurrent][0]
    for s in listAllStops:
        if dicoShortest[s][0]<nextCurrentDist:
            nextCurrent=s
            nextCurrentDist=dicoShortest[s][0]
    return nextCurrent

class ReseauBus:
    def __init__(self):
        self.lignes=[]
        self.allStops=[]


    def addLignes(self,ligne):
        self.lignes.append(ligne)

    def findStops(self,stop): #renvoie une liste des lignes comprenant l'arrret stop
        res=[]
        for e in self.lignes:
            if e.isHere(stop):
                res.append(e)
        return res

    
    def findTheStop(self,stop):
        for e in self.allStops:
            if e.name==stop:
                return e
        return None

    def isAlreadyAdd(self,stop):
        for e in self.allStops:
            if e.name==stop:
                return e
        return None


    def initDicoShortest(self):
        res={}
        for e in self.allStops:
            res[e]=[inf,None]
        return res

    def majDicoDistance(self,current,dico,heure):
        i=0
        for s in current.next_stop:
            newDist=dico[current][0]+self.tempsTraj(heure,current.name,s.name)
            if newDist<dico[s][0]:
                dico[s][0]=newDist
                dico[s][1]=current
            i+=1
        return dico

    def nextBus(self,heure,stopStr,ligne):
        stop=self.findTheStop(stopStr)
        for index in range(len(stop.ligne)):
            if ligne==stop.ligne[index]:
                horraire=stop.horNormales[index][0]
                minHeure=nbmin(heure)
                minHorraire=nbmin(horraire)
                i=0
                while minHeure>minHorraire or i>len(stop.horNormales[index]):
                    i+=1
                    horraire= stop.horNormales[index][i]
                    minHorraire=nbmin(horraire)
        return horraire

    def tempsTraj(self,heure,stopStr,toStr):
        stop=self.findTheStop(stopStr)
        to=self.findTheStop(toStr)
        for index in range(len(stop.next_stop)):
            ns=stop.next_stop[index]
            if ns==to:
                ligne=stop.ligne[index]
                return abs(nbmin(self.nextBus(heure,ns.name,ligne))-nbmin(self.nextBus(heure,stop.name,ligne)))


    def shortestDijkstra(self,start,end):
        listAllStops=[]
        for e in self.allStops:
            listAllStops.append(e)
        startingStop=self.findTheStop(start)
        endingPoint=self.findTheStop(end)
        dicoShortest=self.initDicoShortest()
        listAllStops.remove(startingStop)
        dicoShortest[startingStop][0]=0
        def shortestBis(self,current,end,listAllStops,dicoShortest):
            if current==end:
                return dicoShortest
            dicoShortest=majDicoArcs(current,dicoShortest)
            newCurrent=getNewCurrent(listAllStops,dicoShortest)
            listAllStops.remove(newCurrent)
            return shortestBis(self,newCurrent,end,listAllStops,dicoShortest)
            
        return shortestBis(self,startingStop,endingPoint,listAllStops,dicoShortest)

    def shortest(self,start,end):
        res=""
        dico=self.shortestDijkstra(start,end)
        for cle,value in dico.items():
            if cle==self.findTheStop(end):
                current=self.findTheStop(end)
                res+="en "+ str(value[0]) + " arcs"+"\n"
                while current!= self.findTheStop(start):
                    res+=str(current)+"\n"
                    current=dico[current][1]
        res+=str(self.findTheStop(start))
        return res

    def fastestDijkstra(self,start,end,heure):
        listAllStops=[]
        for e in self.allStops:
            listAllStops.append(e)
        startingStop=self.findTheStop(start)
        endingPoint=self.findTheStop(end)
        dicoShortest=self.initDicoShortest()
        listAllStops.remove(startingStop)
        dicoShortest[startingStop][0]=0
        def fastestBis(self,current,end,listAllStops,dicoShortest,heure):
            if current==end:
                return dicoShortest
            dicoShortest=self.majDicoDistance(current,dicoShortest,add(heure,dicoShortest[current][0]))
            newCurrent=getNewCurrent(listAllStops,dicoShortest)
            listAllStops.remove(newCurrent)
            return fastestBis(self,newCurrent,end,listAllStops,dicoShortest,heure)
            
        return fastestBis(self,startingStop,endingPoint,listAllStops,dicoShortest,heure)

    def fastest(self,start,end,heure):
        res=""
        dico=self.fastestDijkstra(start,end,heure)
        for cle,value in dico.items():
            if cle==self.findTheStop(end):
                current=self.findTheStop(end)
                res+="en "+ str(value[0]) + " minutes"+"\n"
                while current!= self.findTheStop(start):
                    res+=str(current)+"\n"
                    current=dico[current][1]
        res+=str(self.findTheStop(start))
        return res