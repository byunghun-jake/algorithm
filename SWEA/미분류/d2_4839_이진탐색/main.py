import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # P: 전체 쪽수
    # A: A가 찾아야 할 페이지 수
    # B: B가 찾아야 할 페이지 수
    P, A, B = map(int, input().split())
    
    # A 쪽수 찾기
    count_a = 0
    left = 1
    right = P
    while True:
        # 중간값
        middle = int((left+right)/2)
        count_a += 1
        if A < middle:
            right = middle
        elif A > middle:
            left = middle
        else:
            break

    # B 쪽수 찾기
    count_b = 0
    left = 1
    right = P
    while True:
        middle = int((left+right)/2)
        count_b += 1
        if B < middle:
            right = middle
        elif B > middle:
            left = middle
        else:
            break

    # A와 B 검색 횟수 비교하기
    winner = 0
    if count_a > count_b:
        winner = "B"
    elif count_a < count_b:
        winner = "A"

    print(f"#{tc} {winner}")
































