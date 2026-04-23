import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    small = heapq.nsmallest(1,arr)
    return small[0]

def get_min_4_elements(arr: List[int]) -> List[int]:
    return heapq.nsmallest(4,arr)


def get_min_2_elements(arr: List[int]) -> List[int]:
    asc = heapq.nsmallest(2,arr)
    desc = []
    for i in range(len(asc)):
        desc.append(asc.pop())
    return desc




# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))