import numpy as np
import math
import struct_1 as str; #importuojame sukurtą klasę
import sys
import pandas as pd
sys.stdout.reconfigure(encoding='utf-8')

import pandas as pd

def floyd_warshall(graph):
    virsuniu_skaicius=len(graph)
    atstumai = np.full((virsuniu_skaicius, virsuniu_skaicius), np.inf)
        
    for i in range(virsuniu_skaicius):
        atstumai[i][i] = 0    
        for sekantis, svoris in graph[i].edges.items():
            atstumai[graph[i].virsunes_id-1][sekantis-1] = svoris
        
    for k in range(virsuniu_skaicius):
        for i in range(virsuniu_skaicius):
            for j in range(virsuniu_skaicius):
                atstumai[i][j] = min(atstumai[i][j], atstumai[i][k] + atstumai[k][j])                
    return atstumai;


#Sukuriam objektus: virsunes
virsune1 = str.Virsune(1) #sukuriam viršūnę su id 1

virsune2 = str.Virsune(2) 
virsune3 = str.Virsune(3) 
virsune4 = str.Virsune(4) 
#Sukuriam krastines kurios jungia virsunes tarpusavyje
virsune1.add_edge(virsune3, -2) #sukuriam krastinę iš viršūnės 1 į 3 su svoriu -2
virsune3.add_edge(virsune4, 2) 
virsune4.add_edge(virsune2, -1)
virsune2.add_edge(virsune3, 3) 
virsune2.add_edge(virsune1, 4) 

 
print(virsune1.edges[3]) #spausdinam krastinę iš viršūnės 1 į 3
graph = [virsune1, virsune2, virsune3, virsune4]
atstumai = floyd_warshall(graph)
print(atstumai)
