from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """Check if we can finish all courses (check for cycles in a graph)."""
    edges = {}
    for pr in prerequisites: # graph of adjacent nodes
        if pr[0] in edges:
            edges[pr[0]].append(pr[1])
        else:
            edges[pr[0]] = [pr[1]]

    unmarked = list(range(numCourses))
    temp_marks = []

    def visit(idx):
        if idx not in unmarked:
            return True
        if idx in temp_marks:
            return False

        temp_marks.append(idx)
        if idx in edges:
            for j in edges[idx]:
                if visit(j) == False:
                    return False

        temp_marks.remove(idx)
        unmarked.remove(idx)
        return True

    while len(unmarked) > 0:
        if visit(unmarked[0]) == False:
            return False

    return True

print(canFinish(3, [[0,1], [0,2], [1,2]]))