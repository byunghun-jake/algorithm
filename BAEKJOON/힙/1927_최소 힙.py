# heapq: 기본적으로 최소힙을 구현하도록 되어있다.
import heapq
import sys

heap = []

# N: 연산 횟수 (~100,000)
N = int(input())

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)

