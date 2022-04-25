#!/usr/bin/python3
#-*-coding:utf-8-*-
from Ligne import *
from Stop import *
from ReseauBus import *
import data2py1
import data2py2
       


def imple(num,sens):
    i=0
    if num==1 and sens==True:
        stop = Stop(list(data2py1.regular_date_go.keys())[0])
        regular=data2py1.regular_date_go
        hol=data2py1.we_holidays_date_go
        ligne=Ligne(data2py1.data_file_name[0])
    elif num==1 and sens==False:
        stop = Stop(list(data2py1.regular_date_back.keys())[0])
        regular=data2py1.regular_date_back
        hol=data2py1.we_holidays_date_back
        ligne=Ligne(data2py1.data_file_name[0])
    elif num==2 and sens==True:
        stop = Stop(list(data2py2.regular_date_go.keys())[0])
        regular=data2py2.regular_date_go
        hol=data2py2.we_holidays_date_go
        ligne=Ligne(data2py2.data_file_name[0])
    elif num==2 and sens==False:
        stop = Stop(list(data2py2.regular_date_back.keys())[0])
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
            stop.add_next_stop(Stop(str(list(regular.keys())[i+1])))
            stop.next_stop[len(stop.next_stop)-1].add_ligne(ligne)
            #ajout de l'arret de derpart de la ligne
            if i==0: 
                ligne.addStart(stop)
            stop=stop.next_stop[len(stop.next_stop)-1]
        i+=1
    return ligne


ligne1go=imple(1,True)
ligne1back=imple(1,False)
ligne2go=imple(2,True)
ligne2back=imple(2,False)
lignes=[ligne1go,ligne1back,ligne2go,ligne2back]
sybra=ReseauBus(lignes)
print(sybra.shortest("GARE","France_Barattes"))
# print(ligne1go.findStop("GARE"))
#print(ligne2go.tempsTraj('7:00','Courier','Pommaries'))