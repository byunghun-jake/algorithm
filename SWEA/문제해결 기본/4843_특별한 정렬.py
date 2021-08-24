# 1, 2, 3, 4, 5

# 1, 2, 3, 4, 5, 6
# idx: 0 / -1 / 1 / -2 / 2 / -3

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    NUMS = deque(sorted(list(map(int, input().split()))))

    answer = []
    for i in range((N + 1) // 2):
        if len(NUMS):
            answer.append(NUMS.pop())
        if len(NUMS):
            answer.append(NUMS.popleft())
    print(f"#{tc}", *answer[:10])


##############
# T = int(input())
# for tc in range(1, T+1):
#     # N: 배열의 길이
#     # arr: 원본 배열
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     # 오름차순 정렬(선택정렬)
#     for i in range(N-1):
#         min_idx = i
#         for j in range(i+1, N):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         # 교환
#         if i != min_idx:
#             arr[i], arr[min_idx] = arr[min_idx], arr[i]
#
#     # print(arr)
#     # 양 끝의 값을 새 배열에 추가
#     start = 0
#     end = N-1
#     # temp_arr = arr[:]
#     result = []
#     while start < end:
#         big_v = arr[end]
#         small_v = arr[start]
#
#         result.append(big_v)
#         end -= 1
#
#         result.append(small_v)
#         start += 1
#     else:
#         # N이 홀수인 경우
#         if start == end:
#             result.append(arr[start])
#
#     print(f"#{tc}", *result[:10])