# T: 테스트케이스 개수
T = int(input())

for tc in range(T):
    test_result = input()
    total_score = 0
    score = 0
    for r in test_result:
        if r == "O":
            score += 1
            total_score += score
        else:
            score = 0

    print(total_score)





























