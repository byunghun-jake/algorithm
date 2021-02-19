# 자기 점수 중 최댓값을 골랐다
# M: 최댓값
# 모든 점수를 점수/M*100으로 고쳤다.

# N: 시험 본 과목의 개수
N = int(input())

# score_list: 점수 입력
score_list = list(map(int, input().split()))

# 최댓값 찾기
M = score_list[0]
for idx in range(N):
    if M < score_list[idx]:
        M = score_list[idx]

# 점수 업데이트 & 점수 합 구하기
total_score = 0
for idx in range(N):
    total_score += score_list[idx]/M*100

# 평균
average_score = total_score / N

print(average_score)




















