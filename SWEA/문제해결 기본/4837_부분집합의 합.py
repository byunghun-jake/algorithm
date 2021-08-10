# 1부터 12까지의 숫자로 이루어진 집합 A

# N개의 원소로 구성된 부분집합 중 그 합이 K인 집합의 개수는?

# 1. N개의 원소로 구성된 부분집합을 만드시오

# def make_sub_set(sub_set):
#     global answer
#     if len(sub_set) == N:
#         if sum(sub_set) == K:
#             answer += 1
#         return
#
#     for num in range(sub_set[-1], 13):
#         if num in sub_set:
#             continue
#         make_sub_set(sub_set + [num])
#
#
#
# T = int(input())
#
#
# for tc in range(1, T + 1):
#     A = list(range(1, 13))
#     N, K = map(int, input().split())
#
#     answer = 0
#
#
#     for i in range(1, 10):
#         make_sub_set([i])
#     print(f"#{tc} {answer}")


def powerset_backtracking(idx, count):
    global answer
    if count == N:
        temp_sum = 0
        for i in range(1, 13):
            if sel[i]:
                temp_sum += i
        if temp_sum == K:
            answer += 1
    if idx == 13:
        return

    # 이번 idx는 포함
    sel[idx] = 1
    powerset_backtracking(idx + 1, count + 1)

    # 이번 idx는 제외
    sel[idx] = 0
    powerset_backtracking(idx + 1, count)

T = int(input())

for tc in range(1, T + 1):
    A = list(range(1, 13))
    N, K = map(int, input().split())

    answer = 0
    sel = [0] * 13
    powerset_backtracking(1, 0)
    print(answer)