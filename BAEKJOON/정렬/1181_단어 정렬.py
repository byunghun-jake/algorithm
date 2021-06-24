# 시간 제한: 2초
# 메모리 제한: 256MB
# N: 20,000
# 문자의 길이는 최대 50 (1 ~ 50)

# 정렬 기준
    # 1. 길이가 짧은 것 부터
    # 2. 사전 순으로

# 같은 단어가 여러번 입력된 경우에는 한 번씩만 출력한다.
# 입력받은 값의 중복제거가 필요하다.
# 조합

import sys

def merge(left, right):
    result = []
    l_idx = r_idx = 0
    while len(left) > l_idx and len(right) > r_idx:
        if len(left[l_idx]) == len(right[r_idx]):
            if left[l_idx] <= right[r_idx]:
                result.append(left[l_idx])
                l_idx += 1
            else:
                result.append(right[r_idx])
                r_idx += 1
        elif len(left[l_idx]) <= len(right[r_idx]):
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1
    if len(left) > l_idx:
        result += left[l_idx:]
    else:
        result += right[r_idx:]

    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid_idx = len(arr) // 2
    left = mergeSort(arr[:mid_idx])
    right = mergeSort(arr[mid_idx:])

    return merge(left, right)

N = int(sys.stdin.readline().strip())

ARR = [sys.stdin.readline().strip() for _ in range(N)]

sorted_arr = mergeSort(ARR)
for i in range(N):
    if i != 0 and sorted_arr[i - 1] == sorted_arr[i]:
        continue
    print(sorted_arr[i])

