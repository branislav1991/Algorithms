from copy import copy
import math
from typing import List, TypeVar, Callable

T = TypeVar('T')

# ---------------------------- HEAPSORT ------------------------------
def left(lst: List[int], idx: int) -> int:
    """Return left heap child."""
    left_idx = idx * 2 + 1
    if left_idx < len(lst):
        return left_idx
    else:
        return -1

def right(lst: List[int], idx: int) -> int:
    """Return right heap child."""
    right_idx = idx * 2 + 2
    if right_idx < len(lst):
        return right_idx
    else:
        return -1

def max_heapify(lst: List[int], idx: int):
    """Enforce heap property on list. Assumes that children are already heapified."""
    largest = idx
    left_idx = left(lst, idx)
    right_idx = right(lst, idx)
    if left_idx == -1 and right_idx == -1: return # leaf node
    if lst[left_idx] > lst[largest]:
        largest = left_idx
    if lst[right_idx] > lst[largest]:
        largest = right_idx
    if largest != idx:
        tmp = lst[idx] # swap values and heapify on child
        lst[idx] = lst[largest]
        lst[largest] = tmp
        max_heapify(lst, largest)

def build_max_heap(lst: List[int]):
    """Build max heap."""
    for i in range(len(lst)//2-1, -1, -1):
        max_heapify(lst, i)

def heapsort(lst: List[int]) -> List[int]:
    """Sort list using heapsort algorithm."""
    sorted_list = []
    build_max_heap(lst)
    for i in range(len(lst)-1, -1, -1):
        tmp = lst[0] # swap values and heapify on child
        lst[0] = lst[i]
        lst[i] = tmp
        sorted_list.append(tmp)
        lst = lst[:-1]
        max_heapify(lst, 0)
    return sorted_list


# ---------------------------- QUICKSORT ------------------------------
def partition(lst: List[int], a: int, b: int) -> int:
    pivot = lst[b-1]
    j = a
    for i in range(a, b-1):
        if lst[i] < pivot:
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
            j = j + 1
    if j < b-1: # exchange last element if not on border
        tmp = lst[j]
        lst[j] = pivot
        lst[b-1] = tmp
        j = j + 1
    return j

def quicksort(lst: List[int], a: int = 0, b: int = -1) -> List[int]:
    if b == -1: b = len(lst)
    if a + 1 == b: return lst
    split = partition(lst, a, b)
    quicksort(lst, a, split)
    quicksort(lst, split, b)
    return lst


# ---------------------------- COUNTING SORT ------------------------------
def counting_sort(lst: List[int], minimum, maximum) -> List[int]:
    def to_range(v: int) -> int:
        return abs(v - minimum)

    count = [0] * (maximum - minimum + 1) # store number of keys with a certain value
    output = [0] * len(lst)
    for l in lst:
        count[to_range(l)] = count[to_range(l)] + 1
    for i in range(1, len(count)): # build running sum
        count[i] = count[i] + count[i - 1]
    for i in range(len(lst)-1, -1, -1):
        output[count[to_range(lst[i])]-1] = lst[i]
        count[to_range(lst[i])] = count[to_range(lst[i])] - 1
    return output

# ---------------------------- RADIX SORT ------------------------------
def radix_sort(lst: List[List[int]]) -> List[List[int]]: # sort integers written in their decimal form
    output = []
    if not all([len(l) == len(lst[0]) for l in lst[1:]]): raise ValueError("Incorrect input for radix sort") # check if all lengths are equal
    for l in list(zip(*lst))[::-1]:
        output.insert(0, counting_sort(l, 0, 9))
    return list(zip(*output))

# ---------------------------- OTHER SORTS ------------------------------
def insertion_sort(lst: List[int], reverse=False) -> List[int]:
    """Sort input using insertion sort algorithm."""
    lst = copy(lst)
    if len(lst) < 2: return lst
    
    if not reverse:
        for i in range(1, len(lst)):
            key = lst[i]
            j = i - 1
            while j >= 0 and lst[j] > key:
                lst[j+1] = lst[j]
                j = j - 1
            lst[j+1] = key
    else:
        for i in range(len(lst)-2, -1, -1):
            key = lst[i]
            j = i + 1
            while j < len(lst) and lst[j] > key:
                lst[j-1] = lst[j]
                j = j + 1
            lst[j-1] = key
    return lst

def selection_sort(lst: List[int]) -> List[int]:
    """Sort input using selection sort algorithm."""
    lst = copy(lst)
    if len(lst) < 2: return lst

    for i in range(len(lst)-1):
        min_elem = i # find smallest element of sublist
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min_elem]: min_elem = j
        tmp = lst[i]
        lst[i] = lst[min_elem]
        lst[min_elem] = tmp
    return lst

def merge(lst1: List[int], lst2: List[int]) -> List[int]:
    lst = []
    lst1.append(math.inf)
    lst2.append(math.inf)
    for k in range(len(lst1) + len(lst2) - 2):
        if lst1[0] < lst2[0]:
            lst.append(lst1[0])
            lst1.pop(0)
        else:
            lst.append(lst2[0])
            lst2.pop(0)
    return lst

def merge_sort(lst: List[int]) -> List[int]:
    """Merge sort algorithm."""
    lst = copy(lst)
    if len(lst) < 2: return lst

    delim = len(lst) // 2
    l1 = merge_sort(lst[:delim])
    l2 = merge_sort(lst[delim:])
    return merge(l1, l2)


def reverse(lst: List[int]) -> List[int]:
    """Reverses the list."""
    lst = copy(lst)
    if len(lst) < 2:
        return lst

    return lst[::-1]

def linear_search(lst: List[int], val: int) -> int:
    for i in range(len(lst)):
        if lst[i] == val:
            return i
    return -1
 
if __name__ == '__main__':
    x: List[int] = [3, 2, 4, 8, 1, 0, -4]
    y = heapsort(x)[::-1]
    print(f'List {x} converted to {y}')
    y = quicksort(x)
    print(f'List {x} converted to {y}')
    y = counting_sort(x, -4, 8)
    print(f'List {x} converted to {y}')
    y = insertion_sort(x)
    print(f'List {x} converted to {y}')
    z = selection_sort(x)
    print(f'List {x} converted to {z}')
    s = merge_sort(x)
    print(f'List {x} converted to {s}')

    a = [1,9,5,3]
    b = [1,9,7,2]
    c = [2,0,0,2]
    d = [2,1,2,2]
    e = [0,1,2,2]
    f = [0,0,3,9]
    out = radix_sort([f, b, c, a, d, e])
    for item in out:
        print(f'{"".join(map(str, item))}')