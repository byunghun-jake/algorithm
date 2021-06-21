# 나이순 정렬 & 가입순 정렬
# 정렬을 하더라도, 가입한 인덱스를 가지고 있어야겠다.
# 처음 저장할 때, 가입 순서도 저장하는 것으로 (나이, 이름, 가입 순서)
# N = 100,000
# 병합 정렬로 해보자!

import sys

def merge(left, right):
    result = []
    L = len(left)
    R = len(right)
    l_idx = r_idx = 0

    while l_idx < L and r_idx < R:
        # left 배열에 있는 값과 right 배열에 있는 값의 나이가 같다면?
        if left[l_idx][0] == right[r_idx][0]:
            # 가입 순서를 비교한다.
            if left[l_idx][2] < right[r_idx][2]:
                result.append(left[l_idx])
                l_idx += 1
            else:
                result.append(right[r_idx])
                r_idx += 1
        # 나이가 다르다면, 나이가 작은 사람이 먼저
        elif left[l_idx][0] < right[r_idx][0]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1

    # left, right 중 남은 배열을 result 배열의 끝에 붙여줍니다.
    if l_idx < L:
        result += left[l_idx:]
    elif r_idx < R:
        result += right[r_idx:]

    return result

def mergeSort(arr):
    # 종료조건
    if len(arr) <= 1:
        return arr

    # 반으로 나눈 후 다음 나누기로 진행
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    return merge(left, right)


N = int(sys.stdin.readline().strip())
USERS = []
for i in range(N):
    age, name = list(sys.stdin.readline().strip().split())
    user = [int(age), name, i]
    USERS.append(user)

# print(USERS)

sorted_users = mergeSort(USERS)

for user in sorted_users:
    print(*user[:2])