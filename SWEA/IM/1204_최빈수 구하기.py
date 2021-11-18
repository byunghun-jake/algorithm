# 학생의 점수 범위가 정해져 있기 때문에 리스트에 점수들을 카운트해서 넣는 방식으로 하면 될 것 같다.

T = int(input())

for _ in range(T):
    tc = int(input())
    score_list = list(map(int, input().split()))
    score_counter = [0] * 101
    for score in score_list:
        score_counter[score] += 1

    max_count = 0
    max_score = 0
    for i in range(101):
        if max_count <= score_counter[i]:
            max_count = score_counter[i]
            max_score = i
    print(max_score)