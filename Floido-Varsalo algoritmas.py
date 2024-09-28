import numpy as np
import math
import struct_1 as str; #importuojame sukurtą klasę
import sys
import pandas as pd
sys.stdout.reconfigure(encoding='utf-8')

import pandas as pd
def nuskaitymas(filepath):
    zodynas = {} 
    with open(file_path, 'r') as file:
        for line in file:
            airport, connections = line.split(':')
            airport = airport.strip()  
            connections = connections.strip().split(',')  
            
     
            flights = []
            for connection in connections:
                destination, price = connection.split()  
                flights.append((destination, int(price)))  
            
            zodynas[airport] = flights
    
    return zodynas

def floyd_warshall(graph):
    virsuniu_skaicius=len(graph)
    atstumai = np.full((virsuniu_skaicius, virsuniu_skaicius), np.inf)
        
    for i in range(virsuniu_skaicius):
        atstumai[i][i] = 0    
        for sekantis, svoris in graph[i].edges.items():
            atstumai[graph[i].virsunes_id][sekantis] = svoris
        
    for k in range(virsuniu_skaicius):
        for i in range(virsuniu_skaicius):
            for j in range(virsuniu_skaicius):
                atstumai[i][j] = min(atstumai[i][j], atstumai[i][k] + atstumai[k][j])                
    return atstumai;

   
##############################################
#Duomenys iš pavyzdžio:
#Sukuriam objektus: virsunes
# virsune1 = str.Virsune(0) #sukuriam viršūnę su id 0

# virsune2 = str.Virsune(1) 
# virsune3 = str.Virsune(2) 
# virsune4 = str.Virsune(3) 
# #Sukuriam krastines kurios jungia virsunes tarpusavyje
# virsune1.add_edge(virsune3, -2) #sukuriam krastinę iš viršūnės 1 į 3 su svoriu -2
# virsune3.add_edge(virsune4, 2) 
# virsune4.add_edge(virsune2, -1)
# virsune2.add_edge(virsune3, 3) 
# virsune2.add_edge(virsune1, 4) 

# print(virsune2) 
# print(virsune1.edges[3]) #spausdinam krastinę iš viršūnės 1 į 3
# graph = [virsune1, virsune2, virsune3, virsune4]
# atstumai = floyd_warshall(graph)
# print(atstumai)
##############################################
#Oro uostai:
grafas=[]
indeksai={}
file_path ="C:/Users/danie/Downloads/Airport_Distance_Dataset.csv"
duomenys=nuskaitymas(file_path)
Oro_uostai = list(duomenys.keys())
for i in range(len(Oro_uostai)):
    indeksai[Oro_uostai[i]]=i  
numeris=0
for oro_uostas in Oro_uostai:
    temp=str.Virsune(numeris)
    numeris+=1
    for connection in duomenys[oro_uostas]:
        temp.add_edge(str.Virsune(indeksai.get(connection[0])), connection[1])
    grafas.append(temp)


rezultatas = floyd_warshall(grafas)
print(pd.DataFrame(rezultatas, columns=indeksai.keys(), index=indeksai.keys()))
