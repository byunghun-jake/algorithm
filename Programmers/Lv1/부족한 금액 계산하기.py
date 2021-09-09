def solution(price, money, count):
    answer = -1
    total_price = 0
    # 탄 횟수 만큼 곱해진 비용을 축적한다.
    for i in range(1, count + 1):
        total_price += price * i
    # 모자라는 지 확인
    if money >= total_price:
        answer = 0
    else:
        answer = total_price - money
    return answer