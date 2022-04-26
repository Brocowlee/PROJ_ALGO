from Stop import *

class Ligne:
    def __init__(self,num):
        self.num=num
        self.start=None
        self.direction=None

    def __str__(self):
        res = "ligne n°" + self.num +" -"
        stop=self.start
        while stop != self.direction:
            res+=stop.get_name()+"\n"
            stop=stop.get_next_stop(self.num)
            res+="_____"
            for e in stop.next_stop:
                res+=str(e)
            res+="_____"
        res+=" direction: " + self.direction.get_name()
        return res

    def addStart(self,start):
        self.start=start

    def addDirection(self,direction):
        self.direction=direction


#pour avoir le temps de trajet entre 2 arrets d'une ligne
    def tempsTraj(self,heure,stop1,stop2):
        stop=self.start
        res=0
        lastHor=0
        while stop!=self.findStop(stop1):
            stop=stop.get_next_stop(self)
        res+=sub(self.nextBus(heure,stop.name),heure)
        while stop!=self.findStop(stop2):
            if lastHor!=0:
                res+=sub(self.nextBus(lastHor,stop.name),lastHor)
            lastHor=self.nextBus(heure,stop.name)
            stop=stop.get_next_stop(self)
        res+=sub(self.nextBus(lastHor,stop.name),lastHor)
        return res



    def nextBus(self,heureDepart,start):
        start=self.findStop(start)
        ligneStop=start.ligne[0]
        indLigne=0
        indHorraires=0
        while self != ligneStop or indLigne>len(start.ligne):
            indLigne+=1
            ligneStop=start.ligne[indLigne]
        horraire=nbmin(start.horNormales[indLigne][0])
        while horraire < nbmin(heureDepart) or indHorraires>len(start.horNormales[indLigne]):
            indHorraires+=1
            horraire=nbmin(start.horNormales[indLigne][indHorraires])
        return start.horNormales[indLigne][indHorraires]
        
    def findStop(self,stop):
        res=self.start
        try:
            while res.name != stop:
                res = res.get_next_stop(self)
            return res
        except AttributeError:
            return None



#pour avoir le nombre d'arrets entre 2 arrets d'une ligne
    def nbStop(self,stop1,stop2):
        stop=self.start
        secu=0
        res=0
        while stop!=stop1 or secu>=50:
            stop=stop.get_next_node
        if secu==50:
            return None
        while stop!=stop2:
            res+=1
        return res

    def isHere(self,stopName):
        try:
             stop = self.findStop(stopName)
             return True
        except:
            return False
