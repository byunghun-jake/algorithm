# 1. A 업체에 내는 돈을 계산한다.
# 2. B 업체에 내는 돈을 계산한다.
# 2-1. 기본량을 기준으로 추가 사용하는 지 조건을 통해 확인한다.
# 3. 두 업체 중 작은 값을 출력한다.

import sys

sys.stdin = open("./input.txt")

T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    # P: A업체 리터당 요금
    # Q: B업체 기본요금
    # R: B업체 기본제공량
    # S: B업체 리터당 추가 요금
    # W: 사용량

    a_fee = P * W
    b_fee = Q
    if W > R:
        b_fee += (W-R) * S

    result = a_fee
    if a_fee > b_fee:
        result = b_fee

    print(f"#{test_case} {result}")
