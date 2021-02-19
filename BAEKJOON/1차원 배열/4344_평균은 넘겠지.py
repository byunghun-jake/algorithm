# C: 테스트 케이스의 개수
C = int(input())

for tc in range(C):
    N, *arr = list(map(int, input().split()))
    # 평균 구하기
    total_score = 0
    for score in arr:
        total_score += score
    avg = total_score/N

    # 평균 이상의 학생 수 세기
    cnt = 0
    for score in arr:
        if score > avg:
            cnt += 1

    result = cnt / N * 100
    print(f"{result:.3f}%")





























