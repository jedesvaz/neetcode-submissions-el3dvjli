import heapq
from typing import List


def heap_pop(heap: List[int]) -> List[int]:
    #heapq.heappush(heap, 1000)
    lista = []
    while len(heap) != 0:
        lista.append(heapq.heappop(heap))
    return lista


# do not modify below this line
print(heap_pop([1, 2, 3]))
print(heap_pop([1, 3, 2]))
print(heap_pop([6, 7, 8, 12, 9, 10]))
