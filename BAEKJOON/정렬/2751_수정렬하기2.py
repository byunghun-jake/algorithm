# 숫자가 들어오면 배열에 저장한다.
# 저장한 배열을 정렬하여, 오름차순으로 출력한다.
# N <= 1,000,000
    # O(nlogn)으로 해결해야 하는 문제
    # selectionSort로는 시간초과가 발생할 것 같다.

import sys
sys.setrecursionlimit(10000000)

# def getPartition(arr, begin, end):
#     L = begin
#     R = end
#     pivot = (begin + end) // 2
#     while L < R:
#         while arr[L] < arr[pivot] and L < R:
#             L += 1
#         while arr[pivot] <= arr[R] and L < R:
#             R -= 1
#
#         # L위치 탐색과 R위치 탐색 과정이 끝났다면 결과는 둘 중 하나이다.
#             # 1. L < R인 경우
#             # 2. L == R인 경우
#         if L < R:
#             # arr[R] < arr[pivot] <= arr[L]인 경우이다.
#             # L과 pivot이 같을 때, R과 값을 교환하면 pivot의 값이 변하게 되므로,
#             # pivot을 R로 교체한다.
#             if L == pivot:
#                 pivot = R
#             # arr[L]과 arr[R] 값을 교환한다.
#             arr[L], arr[R] = arr[R], arr[L]
#     # L == R인 경우
#     # arr[pivot]과 arr[L]을 교환한다.
#     arr[L], arr[pivot] = arr[pivot], arr[L]
#     return L
#
#
#
# def quickSort(arr, begin, end):
#     # 퀵 정렬을 수행하기 위해서는 begin은 항상 end보다 작아야 한다.
#     if begin >= end:
#         return
#     if begin < end:
#         # 다음 퀵 정렬을 수행할 파티션을 구한다.
#         p = getPartition(arr, begin, end)
#         quickSort(arr, begin, p - 1)
#         quickSort(arr, p + 1, end)

# 5
# 5
# 4
# 3
# 2
# 1

def merge(left, right):
    result = []

    # pop을 사용하면 시간이 너무 오래걸리기 때문에, 대안책을 사용한다.
    left_count, right_count = 0, 0

    while len(left) > left_count and len(right) > right_count:
        if left[left_count] <= right[right_count]:
            result.append(left[left_count])
            left_count += 1
        else:
            result.append(right[right_count])
            right_count += 1

    while len(left) > left_count:
        result.append(left[left_count])
        left_count += 1
    while len(right) > right_count:
        result.append(right[right_count])
        right_count += 1

    return result

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


N = int(sys.stdin.readline())
ARR  = []
for i in range(N):
    ARR.append(int(sys.stdin.readline()))

sortedARR = merge_sort(ARR)
for i in sortedARR:
    print(i)