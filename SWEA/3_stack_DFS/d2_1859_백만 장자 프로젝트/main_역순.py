import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))[::-1]
    
    # 가장 첫 값을 최대값으로 (어차피 마지막 날이라 팔지 못함)
    # 현재 값이 최대값보다 크다면, 최대값을 교체
    # 현재 값이 최대값보다 작다면, 차이만큼 이익

    highest_price = arr[0]
    revenue = 0
    for i in range(1, N):
        if highest_price <= arr[i]:
            highest_price = arr[i]
        else:
            revenue += highest_price - arr[i]

    print(f"#{tc} {revenue}")

























