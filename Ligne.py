from Stop import *

class Ligne:
    def __init__(self,num):
        self.num=num
        self.start=None
        self.direction=None

    def __str__(self):
        res = "ligne n°" + self.num +" -"
        stop=self.start
        # while stop != self.direction:
        #     res+=stop.get_name()+"\n"
        #     stop=stop.get_next_stop(self.num)
        #     res+="_____"
        #     for e in stop.next_stop:
        #         res+=str(e)
        res+=" direction: " + self.direction.get_name()
        return res

    def addStart(self,start):
        self.start=start

    def addDirection(self,direction):
        self.direction=direction


        
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
