# 절대값이 가장 작은 값을 출력한다.
# heap에 넣을 때 절대값으로 변환한 뒤에 넣어주어야 한다.
# -1과 1이 들어있을 때, -1이 먼저 나와야 하기 때문에 음수가 몇 개 들어갔는지 알아야 한다.

import heapq
import sys

N = int(input())

heap = []
store = {}

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    # if num == 0:
    #     if len(heap) == 0:
    #         print(0)
    #     else:
    #         pop_number = heapq.heappop(heap)
    #         if store.get(pop_number):
    #             print(-pop_number)
    #             store[pop_number] -= 1
    #         else:
    #             print(pop_number)
    # else:
    abs_num = abs(num)
    if num < 0:
        if store.get(abs_num):
            store[abs_num] += 1
        else:
            store[abs_num] = 1
    heapq.heappush(heap, abs_num)
    print(heap)


# 튜플을 넣어도 된다.
# import heapq
# import sys
#
# N = int(input())
# heap = []
#
# for _ in range(N):
#     num = int(sys.stdin.readline())
#     if num == 0:
#         if len(heap) > 0:
#             print(heapq.heappop(heap)[1])
#         else:
#             print(0)
#     else:
#         heapq.heappush(heap,(abs(num),num))