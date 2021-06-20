# 최대 N: 10,000,000 (1천만) => O(nlogn)에 해당하는 알고리즘을 사용해야 한다.
#
# 수의 최대 크기: 10,000
    # 수의 크기가 개수에 비해 상대적으로 작기 때문에 카운팅정렬을 사용해보자.

import sys
N = int(sys.stdin.readline())
N_MAX = 10001
count_arr = [0] * N_MAX

for _ in range(N):
    num = int(sys.stdin.readline())
    count_arr[num] += 1

for i in range(N_MAX):
    count = count_arr[i]
    for _ in range(count):
        print(i)
