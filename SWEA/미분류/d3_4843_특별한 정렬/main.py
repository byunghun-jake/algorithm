# 1. 오름차순으로 정렬한다.
# 2. 정렬한 배열을 반으로 나눈다.
# 3. 반복문을 순회하며, 반환할 새 배열에 하나씩 담는다.
import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # N: 배열의 길이
    # arr: 원본 배열
    N = int(input())
    arr = list(map(int, input().split()))

    # 원본 배열을 오름차순으로 정렬한다.
    # 선택정렬
    for i in range(N):
        min_index = i
        for j in range(i+1, N):
            if arr[j] < arr[min_index]:
                min_index = j
        else:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    # 배열을 반으로 나눈다.
    mid_index = N // 2 + N % 2
    small_arr = arr[:mid_index]
    big_arr = arr[mid_index:]
    # print(small_arr, big_arr)

    # 두 배열을 하나로 합친다.

    # 생각하지 못했던 것
    # small_arr는 오름차순
    # big_arr는 내림차순

    # big_arr을 내림차순으로 재정렬
    for i in range(len(big_arr)):
        max_index = i
        for j in range(i+1, len(big_arr)):
            if big_arr[j] > big_arr[max_index]:
                max_index = j
        big_arr[max_index], big_arr[i] = big_arr[i], big_arr[max_index]

    # print(small_arr, big_arr)
    result_arr = []
    for idx in range(mid_index):
        result_arr.append(big_arr[idx])
        result_arr.append(small_arr[idx])
    print(f"#{tc}", *result_arr[:10])



























