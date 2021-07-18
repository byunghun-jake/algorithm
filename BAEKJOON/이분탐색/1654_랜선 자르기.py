# K개의 랜선이 있다.

# N개 이상의(적어도 N개) 랜선을 만들고 싶다.
# 모든 랜선의 길이는 같아야 한다.

# 가능한한 긴 랜선을 만들려고 할 때, 랜선의 길이는?

## 중요
# 1.

N, K = map(int, input().split())

LANS = [int(input()) for _ in range(N)]


# 1. 반복문
min_length = 1
max_length = max(LANS)
while min_length <= max_length:
    mid_length = (max_length + min_length) // 2
    count = 0
    for lan in LANS:
        count += lan // mid_length

    if count >= K:
        min_length = mid_length + 1
    else:
        max_length = mid_length - 1
print(max_length)

# 2. 재귀 (X, 깊이 문제)
# def binary_search(min_length, max_length):
#     if min_length >= max_length:
#         print(max_length)
#         return
#
#     mid_length = (max_length + min_length) // 2
#     count = 0
#     for lan in LANS:
#         count += lan // mid_length
#
#     if count >= K:
#         binary_search(mid_length + 1, max_length)
#     else:
#         binary_search(min_length, mid_length - 1)
# binary_search(1, max(LANS))