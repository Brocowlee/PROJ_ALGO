#!/usr/bin/python3
#-*-coding:utf-8-*-
from Ligne import *
from Stop import *
from ReseauBus import *
import data2py1
import data2py2
       


def imple(num,sens,reseau):
    i=0
    if num==1 and sens==True:
        if reseau.isAlreadyAdd(Stop(list(data2py1.regular_date_go.keys())[0])) == None:
            stop = Stop(list(data2py1.regular_date_go.keys())[0])
        else:
            stop = reseau.isAlreadyAdd(Stop(list(data2py1.regular_date_go.keys())[0]))
        regular=data2py1.regular_date_go
        hol=data2py1.we_holidays_date_go
        ligne=Ligne(data2py1.data_file_name[0])
    elif num==1 and sens==False:
        if reseau.isAlreadyAdd(Stop(list(data2py1.regular_date_back.keys())[0])) == None:
            stop = Stop(list(data2py1.regular_date_back.keys())[0])
        else:
            stop = reseau.isAlreadyAdd(Stop(list(data2py1.regular_date_back.keys())[0]))
        regular=data2py1.regular_date_back
        hol=data2py1.we_holidays_date_back
        ligne=Ligne(data2py1.data_file_name[0])
    elif num==2 and sens==True:
        if reseau.isAlreadyAdd(Stop(list(data2py2.regular_date_go.keys())[0])) == None:
            stop = Stop(list(data2py2.regular_date_go.keys())[0])
        else:
            stop = reseau.isAlreadyAdd(Stop(list(data2py2.regular_date_go.keys())[0]))
        regular=data2py2.regular_date_go
        hol=data2py2.we_holidays_date_go
        ligne=Ligne(data2py2.data_file_name[0])
    elif num==2 and sens==False:
        if reseau.isAlreadyAdd(Stop(list(data2py2.regular_date_back.keys())[0])) == None:
            stop = Stop(list(data2py2.regular_date_back.keys())[0])
        else:
            stop = reseau.isAlreadyAdd(Stop(list(data2py2.regular_date_back.keys())[0]))
        regular=data2py2.regular_date_back
        hol=data2py2.we_holidays_date_back
        ligne=Ligne(data2py2.data_file_name[0])
    else:
        return None
    for cle,val in regular.items():
        if i==len(list(regular.keys()))-1:
            ligne.addDirection(stop)
        else:
            stop.add_horNormales(val)
            stop.add_horVancances(hol[cle])
            stop.add_ligne(ligne)
            #fix du probleme?
            if reseau.isAlreadyAdd(str(list(regular.keys())[i+1]))==None:
                newStop=Stop(str(list(regular.keys())[i+1]))
                stop.add_next_stop(newStop)
                reseau.allStops.append(newStop)
            else:
                stop.add_next_stop(reseau.isAlreadyAdd(str(list(regular.keys())[i+1])))

            stop.next_stop[len(stop.next_stop)-1].add_ligne(ligne)
            #ajout de l'arret de derpart de la ligne
            if i==0: 
                ligne.addStart(stop)
            stop=stop.next_stop[len(stop.next_stop)-1]
        i+=1
    return ligne

sybra=ReseauBus()
ligne1go=imple(1,True,sybra)
sybra.addLignes(ligne1go)
ligne1back=imple(1,False,sybra)
sybra.addLignes(ligne1back)
ligne2go=imple(2,True,sybra)
sybra.addLignes(ligne2go)
ligne2back=imple(2,False,sybra)
sybra.addLignes(ligne2back)

#print(sybra.shortestDijkstra("Ponchy","Vernod"))
# for e in sybra.findTheStop("GARE").get_next_stops():
#     print(e)
# print(ligne2go.direction)
for e in sybra.allStops:
    print(e)
#print(len(ligne1go.findStop("Ponchy").next_stop))
#print(ligne2go.tempsTraj('7:00','Courier','Pommaries'))