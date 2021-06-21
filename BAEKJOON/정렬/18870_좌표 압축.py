# 입력한 좌표들 중에서 자기 자신보다 작은 좌표의 개수를 값으로 갖는 배열로 변환
# N = 1,000,000
# -10^9 <= xi < 10^9
# 시간 제한: 2초
# 메모리 제한: 512MB


# x의 범위가 크기 때문에 카운팅 정렬은 적합하지 않다.
# 1,000,000,000 (10억)

# set을 이용해서 정렬을 한 뒤, 원본 배열을 돌며 정렬된 배열에서 해당하는 인덱스를 찾아 출력

import sys

N = int(sys.stdin.readline().strip())
NODES = list(map(int, sys.stdin.readline().strip().split()))


def merge(left, right):
    result = []
    L = len(left)
    R = len(right)
    l_idx = r_idx = 0
    while l_idx < L and r_idx < R:
        if left[l_idx] < right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1
    if l_idx < L:
        result += left[l_idx:]
    else:
        result += right[r_idx:]
    return result


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


# print(NODES)
nodes = list(set(NODES))
# sorted_nodes = mergeSort(nodes)
sorted_nodes = sorted(nodes)

node_dict = {}
for i in range(len(sorted_nodes)):
    node_dict[sorted_nodes[i]] = i

for node in NODES:
    print(node_dict[node], end=" ")
