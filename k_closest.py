import copy
import math
from typing import List

def kClosest(points: List[List[int]], K: int) -> List[List[int]]:
    """Select k closest points to the origin by quickselect."""
    dist = []
    for p in points:
        dist.append(math.sqrt(p[0]**2 + p[1]**2))
        
    # quickselect K points
    def quickselect(di, start, end, k):
        if end-start==1:
            return di[start]

        pivot = di[end-1]
        i = start-1
        for j in range(start, end-1):
            if di[j] < pivot:
                i = i + 1
                di[i], di[j] = di[j], di[i]
        i = i + 1
        di[i], di[end-1] = di[end-1], di[i]
        if (i+1) == k:
            return di[i] # return k-th smallest distance
        elif (i+1) > k:
            return quickselect(di, start, i, k)
        else:
            return quickselect(di, i+1, end, k)
        
    k_smallest = quickselect(copy.copy(dist), 0, len(dist), K)
    # compare with pivot
    result = []
    for i in range(len(dist)):
        if dist[i] <= k_smallest:
            result.append(points[i])
    return result

kClosest([[1,3],[-2,2],[2,-2]], 2)