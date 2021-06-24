# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# N의 최대가 1000이다. O(n^2)까지 가능하다.

# 정렬 방식
    # 1. 선택 정렬
    # 2.

import sys
sys.setrecursionlimit(1000000)

# def selectionSort_recursion(current_idx):
#     if current_idx == N:
#         return
#
#     min_num = ARR[current_idx]
#     min_idx = current_idx
#     for i in range(current_idx, N):
#         if min_num > ARR[i]:
#             min_idx = i
#             min_num = ARR[i]
#     else:
#         ARR[current_idx], ARR[min_idx] = ARR[min_idx], ARR[current_idx]
#     selectionSort_recursion(current_idx + 1)
#
#
# def selectionSort_loop():
#     for c_idx in range(N):
#         min_idx = c_idx
#         for target_idx in range(c_idx + 1, N):
#             if ARR[min_idx] > ARR[target_idx]:
#                 min_idx = target_idx
#         else:
#             ARR[c_idx], ARR[min_idx] = ARR[min_idx], ARR[c_idx]
#
#
# # 버블정렬
# def bubbleSort():
#     print(ARR)
#     for i in range(N-1, 0, -1):
#         for j in range(i):
#             if ARR[j] > ARR[j + 1]:
#                 ARR[j], ARR[j + 1] = ARR[j + 1], ARR[j]
#             print(ARR)
#
# # 퀵정렬
# def makePartition(arr, start, end):
#     L = start
#     R = end
#     pivot = (L + R) // 2
#     while L < R:
#         # pivot 값보다 크거나 같은 값을 찾는 과정
#         # R보다는 항상 작아야 한다.
#         while arr[L] < arr[pivot] and L < R:
#             L += 1
#         # pivot 값보다 작은 값을 찾는 과정
#         # L보다는 항상 커야한다.
#         while arr[pivot] <= arr[R] and L < R:
#             R -= 1
#
#         # 두 값이 교환되지 않은 상태에서 원하는 두 값을 찾았다면,
#             # 서로 교환한다.
#         if L < R:
#             if L == pivot:
#                 # print(arr, arr[L], arr[pivot], arr[R])
#                 # print(start, end)
#                 pivot = R
#                 pass
#             arr[L], arr[R] = arr[R], arr[L]
#     arr[pivot], arr[R] = arr[R], arr[pivot]
#     return L
#
#
# def quickSort(a, start, end):
#     if start < end:
#         p = makePartition(a, start, end)
#         quickSort(a, start, p - 1)
#         quickSort(a, p + 1, end)


# 4. 병합 정렬
def merge(left, right):
    # 두 배열을 병합할 배열 생성
    result = []
    l_idx, r_idx = 0, 0
    while len(left) > l_idx and len(right) > r_idx:
        # 양쪽 리스트 모두 원소가 남아있을 떄,
        # 가장 앞에 있는 원소를 비교하여 작은 값을 결과 배열에 추가해준다.
        if left[l_idx] <= right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1
    # 두 리스트 중 어느 하나라도 원소가 남아있다면?
    if len(left) > l_idx:
        result += left[l_idx:]
    if len(right) > r_idx:
        result += right[r_idx:]

    return result

def merge_sort(arr):
    # 바닥 조건 (더이상 배열을 분할할 수 없을 때)
    if len(arr) <= 1:
        return arr

    # 1. Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # 리스트의 크기가 1이 될 때 까지 merge_sort 함수를 이용하여 쪼갠다.
    left = merge_sort(left)
    right = merge_sort(right)

    # 바닥 조건에 해당하지 않는다면, 리스트의 크기가 1이 될 때까지 나눠진 후 합쳐지는 과정에 있다는 것
    merged_arr = merge(left, right)
    return merged_arr

# N: 수의 개수
# ARR: 수가 담긴 배열

ARR = [4, 1, 3, 2]
new_ARR = merge_sort(ARR)
print(new_ARR)