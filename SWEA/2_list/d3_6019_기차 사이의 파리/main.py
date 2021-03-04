# 파리가 날아가는 거리 = 속도 * 시간
# 두 기차가 만나는 데 걸리는 시간 = 파리가 날아가는 시간
# 두 기차가 만나는 데 걸리는 시간 = 두 기차 간의 거리 / (두 기차의 속도의 합)
import sys, math

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # D: 기차 사이의 거리
    # A: 기차 A의 속력
    # B: 기차 B의 속력
    # F: 파리의 속력
    D, A, B, F = map(int, input().split())

    # # time: 두 기차가 만나는 데 걸리는 시간
    # time = D / (A + B)
    #
    # # s: 파리가 날아간 거리
    # s = time * F

    # 무한 급수로 풀어보자
    # s: 파리가 날아간 거리
    s = 0
    while not math.isclose(D, 0):
        # D는 기차 사이의 거리임과 동시에 파리와 기차 B사이의 거리이기도 하다
        # t1: 파리와 기차 B가 만나는 데 걸리는 시간
        t1 = D / (B + F)
        # 파리가 날아간 거리는 시간 * 속력
        s1 = t1 * F
        # 파리가 날아간 거리에 누적해준다.
        s += s1
        # (파리가 날아간 거리 - 기차 A가 이동한 거리)는 이제 기차 A와 B(파리)간의 거리가 된다.
        D = s1 - (t1 * A)
        # A로 날아가보자.
        t2 = D / (A + F)
        s2 = t2 * F
        D = s2 - (t2 * B)
        s += D

    print(f"#{tc} {s:.6f}")






























