# 단, 점수가 가장 큰 후보가 여러 명인 경우에는
# 3점을 더 많이 받은 후보를 회장으로 결정하고,
# 3점을 받은 횟수가 같은 경우에는 2점을 더 많이 받은 후보를 회장으로 결정한다.
# 동점인 경우 높은 점수를 많이 받은 후보가 이긴다.

# 반 학생들의 수는 최대 1000
    # O(n^2) 가능

# 세 후보에 대한 점수를 저장하는 것 보다는
# [후보 번호, 1점 개수, 2점 개수, 3점 개수, 총점]으로
# 몇 점을 몇 개 받았는지 저장하자.
# 2차원 배열을 선언
# 학생들의 투표 결과를 받을 때, 개수를 세고 합계 점수도 저장한다.
# 배열을 정렬한다.
    # 2점 표의 개수로 정렬
    # 3점 표의 개수로 정렬
    # 총점으로 정렬
# 유일한 한 명이 나올 수 있는지 판단한다.
    # 0번 배열과 1번 배열의 총점과 3점 표의 개수, 2점 표의 개수가 같은지 확인
        # 같다면, 결정할 수 없는 경우 출력
        # 다르다면, 0번 배열의 후보 출력

# 멋진 아이디어
    # 점수가 같아도 높은 점수를 얻은 사람을 쉽게 찾기 위한 방법
        # 점수를 제곱하여 누적한 값을 저장한다.


def selectionSort(arr, idx):
    # idx: 정렬할 기준 인덱스
    for i in range(3 - 1):
        max_idx = i
        for j in range(i, 3):
            if arr[max_idx][idx] < arr[j][idx]:
                max_idx = j
        else:
            arr[i], arr[max_idx] = arr[max_idx], arr[i]

def choiceLeader(arr):
    A = arr[0]
    B = arr[1]
    if A[4] == B[4] and A[3] == B[3] and A[2] == B[2]:
        print(0, A[4])
    else:
        print(A[0], A[4])


N = int(input())

SCORE = [
    [1, 0, 0, 0, 0],
    [2, 0, 0, 0, 0],
    [3, 0, 0, 0, 0],
]

for _ in range(N):
    a, b, c = map(int, input().split())
    SCORE[0][a] += 1
    SCORE[0][4] += a
    SCORE[1][b] += 1
    SCORE[1][4] += b
    SCORE[2][c] += 1
    SCORE[2][4] += c

# print(SCORE)
selectionSort(SCORE, 2)
# print(SCORE)
selectionSort(SCORE, 3)
# print(SCORE)
selectionSort(SCORE, 4)
# print(SCORE)
choiceLeader(SCORE)