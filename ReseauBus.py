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
        
    # def shortest(self,start,end,heure):
    #     def min(old,new):
    #         if new>old:
    #             return old
    #         else :
    #             return new
    #     nbArcs=1000
    #     for e in self.lignes:
    #         if e.isHere(start) and e.isHere(end):
    #             nbArcs=min(e.nbStop,nbArcs)
    #         elif e.isHere(start) and not(e.isHere(end)):
    #             for 

    def shortest(self,start,end):
        startingStop=self.findTheStop(start)
        endingStop=self.findTheStop(end)
        def shortestbis(self,nbArcs,stop,end):
            print(nbArcs)
            if stop==end:
                print(nbArcs)
                return nbArcs
            else:
                for i in range(len(self.findStops(stop))):
                    ligne=self.findStops(stop)[i]
                    if stop.get_next_stop(ligne)==None:
                        print("ici")
                        #return None
                    else:
                        shortestbis(self,nbArcs+1,stop.get_next_stop(ligne),end)
   
        res= shortestbis(self,0,startingStop,endingStop)
        print(res)
        return res
                

        











        # def exploReseau(stopB):
        #     if stopB==end:
        #         nbArcs=min(nbArcs,)
        #     else:
        #         nbArcs+=1
        #     for el in stopB.next_stop:
        #         exploReseau(el)
        # for e in self.lignes:
        #     if e.findStop(start)!=None:
        #         stop=e.findStop(start)


                