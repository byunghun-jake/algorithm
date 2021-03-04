# 현재 지점을 기준으로 가격이 가장 높은 날을 찾는다.
# 현재 지점이 가장 가격이 높다면, 구매하지 않고 파는 날
# 현재 지점보다 가격이 높은 날이 뒤에 있다면, 구매 후 해당 날짜에 판매

# 10 7 6
# 1일차: 현재 기준 가격이 앞날보다 높기 때문에, 구매하지 않는다.
# 2일차: 현재 기준 가격이 앞날가격의 최대값 보다 높기 때문에 구매하지 않는다.
# 3일차: 현재 날짜가 마지막 날이기 때문에 구매하지 않는다.

# 3 5 9
# 1일차: 현재 기준 가격보다 앞날에 더 높은 가격이 있다. 구매한다.
# 2일차: 현재 기준 가격보다 앞날에 더 높은 가격이 있다. 구매한다.
# 3일차: 마지막 날이기 때문에 구매하지 않는다. 지금까지 구매했던 것들을 판다.

# 구매와 판매가 동시에 일어나지는 않는다.
# 현재 날짜와 현재 날짜를 기준으로 앞날의 가격 최대값을 비교하여 구매 / 판매 선택
import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 숫자의 개수
    N = int(input())

    # PRICE_LIST: 가격 배열
    PRICE_LIST = list(map(int, input().split()))

    # 앞날의 최대값을 찾는다.
    # 최대값을 만나고, 그 값 뒤에 다른 값들이 있다면, 또 최대값을 찾는다.
    highest_price = 0
    revenue = 0
    for idx in range(N):
        price = PRICE_LIST[idx]
        # 최대값 찾기
        # 첫 시작을 고려한 조건
        if highest_price <= price:
            highest_price = 0
            for i in range(idx+1, N):
                if highest_price < PRICE_LIST[i]:
                    highest_price = PRICE_LIST[i]

        # 현재 값이 앞날의 최대값보다 작다면, 구매한다.
        if price < highest_price:
            revenue += highest_price - price
        # 현재 값이 찾았던 최대값이라면, 지금까지 구매한 것들을 판다. (스택으로 해결하는 경우)

    print(f"#{tc} {revenue}")













































