# 1. 오름차순으로 정렬한다.
# 2. 양 끝에 있는 값을 가져와 새 배열에 추가한다.

import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # N: 배열의 길이
    # arr: 원본 배열
    N = int(input())
    arr = list(map(int, input().split()))

    # 오름차순 정렬(선택정렬)
    for i in range(N-1):
        min_idx = i
        for j in range(i+1, N):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 교환
        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    # print(arr)
    # 양 끝의 값을 새 배열에 추가
    start = 0
    end = N-1
    # temp_arr = arr[:]
    result = []
    while start < end:
        big_v = arr[end]
        small_v = arr[start]

        result.append(big_v)
        end -= 1

        result.append(small_v)
        start += 1
    else:
        # N이 홀수인 경우
        if start == end:
            result.append(arr[start])
    
    # 10개까지 출력하시오
    print(f"#{tc}", *result[:10])



























