import data2py

def nbmin(h):
    if len(h)==5:
        hbis=h[0]+h[1]
    else:
        hbis=h[0]
    m=h[len(h)-2]+h[len(h)-1]
    return 60*int(hbis)+int(m)

def sub(h1,h2):
    return nbmin(h1)-nbmin(h2)


class Stop:
    def __init__(self,name):
        self.name=name
        self.next_stop=[]
        self.ligne=[]
        self.horNormales=[]
        self.horVacances=[]
    
    def __str__(self):
        return "name: " + self.name

    def add_next_stop(self,nextStop):
        self.next_stop.append(nextStop)

    def add_ligne(self,ligne):
        self.ligne.append(ligne)

    def add_horNormales(self,hor):
        self.horNormales.append(hor)

    def add_horVancances(self,hor):
        self.horVacances.append(hor)

    def get_name(self):
        return self.name

    def get_next_stops(self):
        return self.next_stop

    def get_next_stop(self,ligne):
        i=0
        for e in self.ligne:

            if e==ligne and self.get_next_stops()!=[]:
                return self.get_next_stops()[i]
            elif self.get_next_stops()==[]:
                return None
            else:
                i+=1
        return self.get_next_stops()[0]

    def get_horNormales(self):
        return self.horNormales

    def get_horVacances(self):
        return self.horVacances        
    



class ligne:
    def __init__(self,num):
        self.num=num
        self.start=None
        self.direction=None

    def __str__(self):
        res = "ligne n°" + self.num +"\n"
        stop=self.start
        while stop != self.direction:
            res+=stop.get_name()+"\n"
            stop=stop.get_next_stop(self.num)
        res+=self.direction.get_name()
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
        while res.name != stop:
            res = res.get_next_stop(self)
        return res


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
