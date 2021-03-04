import sys

sys.stdin = open("input.txt")

# 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번 수행
# 수열의 맨 앞에 있는 숫자를 출력하는 프로그램

# 접근방법
    # 1. index를 M만큼 증가시킨 후 나머지연산을 수행하여 최종 인덱스가 가리키는 값을 구하는 방식
    # 2. 수열의 맨 앞의 숫자를 맨 뒤로 보내는 작업을 M회 반복하여, 맨 앞에 있는 숫자를 구하는 방식


def change_queue(_q):
    for _ in range(M):
        # _q.pop(0)을 통해 맨 앞의 값을 뽑아낸다.
        # _q.append()를 통해 맨 뒤로 뽑아낸 값을 추가한다.
        _q.append(_q.pop(0))

    return _q[0]



TC = int(input())
for tc in range(1, TC + 1):
    # N: 수열의 길이
    # M: 수행 횟수
    N, M = map(int, input().split())

    # NUMS: 수열
    NUMS = list(map(int, input().split()))

    # # 1번 방법
    # idx = M % N
    # result = NUMS[idx]

    # 2번 방법
    result = change_queue(NUMS[:])

    print(f"#{tc} {result}")