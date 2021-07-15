N = int(input())
NUMS = list(map(int, input().split()))

result = [-1] * N
stack = [NUMS[-1]]
idx = N - 2
for idx in range(N - 2, -1, -1):
    while stack and NUMS[idx] >= stack[-1]:
        stack.pop()
    if stack and NUMS[idx] < stack[-1]:
        result[idx] = stack[-1]
    stack.append(NUMS[idx])

print(*result)



# N = int(input())
# NUMS = list(map(int, input().split()))
#
# # 각 인덱스의 오큰수가 담길 배열
# result = [-1 for _ in range(N)]
#
# # 오큰수를 찾지 못한 인덱스의 배열
# # 이 배열은 가장 뒤 값이 가장 작다 (내림차순)
# stack = []
#
# for i in range(N):
#     while stack and NUMS[stack[-1]] < NUMS[i]:
#         result[stack[-1]] = NUMS[i]
#         stack.pop()
#
#     stack.append(i)
#
# print(*result)