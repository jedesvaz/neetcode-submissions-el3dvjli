import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []

    for num in nums:
        if num > 0:
            pair = (-abs(num), num)
        else:
            pair = (abs(num), num)
        heapq.heappush(heap, pair)
    listreturn= []
    while heap:
        pair = heapq.heappop(heap)
        listreturn.append(pair[1])
    return listreturn


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
