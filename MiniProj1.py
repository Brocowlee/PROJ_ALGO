import data2py

def nbmin(h):
    if len(h)==5:
        hbis=h[0]+h[1]
    else:
        hbis=h[0]
    m=h[len(h)-2]+h[len(h)-1]
    return 60*int(hbis)+int(m)

def sub(h1,h2):
    return nbmin(h2)-nbmin(h1)

#print(sub("5:54","6:32"))


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
            if e==ligne:
                return self.get_next_stops()[i]
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
    # def tempsTraj(self,stop1,stop2):
    #     stop=self.start
    #     secu=0
    #     res=0
    #     while stop!=stop1 or secu>=50:
    #         stop=stop.get_next_node()
    #     if secu==50:
    #         return None
    #     while stop!=stop2:
    #         res+=stop.get_time
    #     return res

    def nextBus(self,heureDepart,start,end):
        hdMin=nbmin(heureDepart)
        ligneStop=start.ligne[0]
        indLigne=0
        indHorraires=0
        while (self != ligneStop and end == self.direction) or indLigne>len(start.ligne):
            indLigne+=1
            ligneStop=start.ligne[indLigne]
        horraire=nbmin(start.horNormales[indLigne][0])
        while horraire < nbmin(heureDepart) or indHorraires>len(start.horNormales[indLigne]):
            indHorraires+=1
            horraire=nbmin(horraire=start.horNormales[indLigne][indHorraires])
        return start.horNormales[indLigne][indHorraires]
        

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
