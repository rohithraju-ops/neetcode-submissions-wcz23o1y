from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    stack = []
    for i, n in enumerate(arr):
        stack.append(arr[i])
    
    rev_arr = []
    while len(stack) > 0:
        rev_arr.append(stack.pop())
    
    return rev_arr

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
