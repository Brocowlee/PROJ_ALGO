#!/usr/bin/python3
#-*-coding:utf-8-*-

import MiniProj1
import data2py
       


def imple():
    i=0
    stop = MiniProj1.Stop(list(data2py.regular_date_go.keys())[0])
    ligne=MiniProj1.ligne(data2py.data_file_name[0]) #creation ligne vierge avec seulement le numero de la ligne
    for cle,val in data2py.regular_date_go.items():
        if i==len(list(data2py.regular_date_go.keys()))-1:
            ligne.addDirection(stop)
        else:
            stop.add_horNormales(val)
            stop.add_horVancances(data2py.we_holidays_date_go[cle])
            stop.add_ligne(ligne)
            stop.add_next_stop(MiniProj1.Stop(str(list(data2py.regular_date_go.keys())[i+1])))
            stop.next_stop[len(stop.next_stop)-1].add_ligne(ligne)
            #ajout de l'arret de derpart de la ligne
            if i==0: 
                ligne.addStart(stop)
            stop=stop.next_stop[len(stop.next_stop)-1]
        i+=1
    return ligne

ligne=imple()
#print(MiniProj1.sub(ligne.nextBus("7:00","Vernod"),"7:00"))
#print(ligne.nextBus('7:00','Vernod'))
print(ligne.tempsTraj('7:00','Vernod','Meythet_Le_Rabelais'))
#print(MiniProj1.nbmin('5:15'))
#print(sub("5:54","6:32"))
#print(data2py.dates2dic(ligne.start.get_next_stop(ligne).get_horNormales()[0]))
#print(ligne)
#print(ligne.start)