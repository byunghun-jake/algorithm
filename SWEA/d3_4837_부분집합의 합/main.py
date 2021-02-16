import sys

sys.stdin = open("input.txt")


def arr_sum(a):
    total = 0
    for n in a:
        total += n
    return total


T = int(input())
for tc in range(1, T+1):
    # N: 부분칩합 원소 개수
    # K: 부분집합의 합
    N, K = map(int, input().split())

    # 1~12의 숫자를 원소로 가진 집합 A에서
    # 원소의 개수가 N인 모든 부분집합을 구해보자
    # 1. 모든 부분집합을 구한 뒤, 길이가 N인 경우만 고려
    arr = list(range(1, 13))
    L = len(arr)
    count = 0
    for i in range(1 << L):
        temp_arr = []
        for j in range(L):
            if i & 1 << j:
                temp_arr.append(arr[j])
        # temp_arr의 길이가 3인 경우
        if len(temp_arr) == N and arr_sum(temp_arr) == K:
            count += 1
    print(f"#{tc} {count}")





































