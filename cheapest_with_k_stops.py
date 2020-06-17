import math
from typing import List
from heapq import heappop, heappush

def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
    graph = {i: math.inf for i in range(n)}
    graph[src] = 0
    
    flights_dict = {}
    for f in flights:
        if f[0] in flights_dict:
            flights_dict[f[0]].append((f[1], f[2]))
        else:
            flights_dict[f[0]] = [(f[1], f[2])]
    
    heap = [(0,0,src)]
    while heap:
        x = heappop(heap)
        if x[1] > K:
            continue
        
        if x[2] in flights_dict:
            for f in flights_dict[x[2]]:
                graph[f[0]] = min(graph[f[0]], graph[x[2]] + f[1])
                heappush(heap, (graph[f[0]], x[1]+1, f[0]))
            
    return graph[dst] if graph[dst] < math.inf else -1

findCheapestPrice(3, [[0,1,100], [1,2,100], [0,2,500]], 0, 2, 1)