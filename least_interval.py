from collections import Counter
from typing import List

def leastInterval(tasks: List[str], n: int) -> int:
    num_cycles = 0
    tasks = [c for c in Counter(tasks).values()]
    while tasks:
        tasks = sorted(tasks, reverse=True)
        add = 0
        for i in range(n+1):
            if i < len(tasks):
                tasks[i] = tasks[i] - 1
                if tasks[i] < 1:
                    del tasks[i]
                add = add + 1
            elif not tasks:
                break
            else:
                add = add + 1
        num_cycles = num_cycles + add
                
    return num_cycles

print(leastInterval(["A","A","A","B","B","B"], 2))