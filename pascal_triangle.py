from typing import List

def getRow(rowIndex: int) -> List[int]:
    first = [1]
    if rowIndex == 0:
        return first
    
    def row(pre: List[int], n: int):
        if n == rowIndex:
            return pre
        
        nex = [pre[0]]
        for i in range(1, len(pre)):
            nex.append(pre[i-1] + pre[i])
        nex.append(pre[-1])
        return row(nex, n+1)
    
    return row(first, 0)

print(getRow(1))