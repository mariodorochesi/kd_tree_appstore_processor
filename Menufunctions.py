from utils.utils import one_shot_encoding, vectorize, normalize, distance, normalize_excluded
from time import clock
    
def searchByList(list_nodes, toSearch, cant_nodes):
    timeInit = clock()
    similar = []
    r = []
    iterCount = 0
    totalMax = 1000000000000000000
    
    for n in list_nodes:
        d = distance(n.vector,toSearch.vector)
        
        if(len(similar) < cant_nodes and d!=0):
            similar.append(n)
        else:     
            if(d < totalMax and d!=0):
                similar.pop()
                similar.append(n)
                iterCount+=1

        similar = sorted(similar, key = lambda x: distance(toSearch.vector, x.vector) )
        totalMax = distance(similar[-1].vector, toSearch.vector)


    finalTime = clock()
    iterationTime = finalTime - timeInit
    
    for n in similar:
        r.append(distance(n.vector, toSearch.vector))
        
    print(r)
    
    return [similar,[iterationTime,iterCount]]
    