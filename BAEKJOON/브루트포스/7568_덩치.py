# N: 전체 사람의 수
N = int(input())

student_list = []
for _ in range(N):
    student_list.append(tuple(map(int, input().split())))

# print(student_list)

# 학생 리스트를 순환하며, 자기보다 덩치가 큰 학생이 있다면 등수를 1씩 증가시킨다.
rank_list = []
for i in range(N):
    # i 비교 기준 인덱스
    rank = 1
    for j in range(N):
        # j 비교할 인덱스
        if i == j:
            continue
        if student_list[i][0] < student_list[j][0] and student_list[i][1] < student_list[j][1]:
            rank += 1
    rank_list.append(rank)

print(*rank_list)





























