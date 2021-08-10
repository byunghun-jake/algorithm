# 0점 ~ 100점 분포를 보이는 점수의 최빈값을 찾는 문제

T = int(input())

for _ in range(1, T + 1):
    tc = int(input())
    SCORES = list(map(int, input().split()))
    score_counter = [0] * 101

    popular_score = -1
    popular_count = 0
    for score in SCORES:
        score_counter[score] += 1
        if popular_count <= score_counter[score]:
            popular_count = score_counter[score]
            popular_score = score

    print(f"#{tc} {popular_score}")