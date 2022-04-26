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


    def get_next_stop(self,ligne):
        i=0
        for e in self.ligne:
            if e==ligne and self.next_stop!=[]:
                return self.next_stop[i]
            elif self.next_stop==[]:
                return None
            else:
                i+=1
        return self.next_stop[0]

    def get_horNormales(self):
        return self.horNormales

    def get_horVacances(self):
        return self.horVacances