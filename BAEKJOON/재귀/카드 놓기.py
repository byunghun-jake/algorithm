# 4 <= N <= 10
# 1이상 99이하
# K장 선택 (2 ~ 4)
# 상근이가 만들 수 있는 정수는 모두 몇 가지일까?

# 조합 문제
# 카드를 선택할 것인가, 선택하지 않을 것인가
# 선택한 카드를 섞는 방법

def perm(arr, depth, idx):


def comb(arr, idx, count):
    # 카드를 더이상 뽑을 필요가 없을 때
    # 뽑은 카드 수 + 뽑을 수 있는 카드 수 < 뽑아야 하는 카드 수
    if (count + N - idx + 1) < K:
        return
    # 카드를 최대 한도로 뽑았을 때
    if count == K:
        pass
    # 카드를 끝까지 뽑았을 때
    if idx == N - 1:


N = int(input())
K = int(input())
CARDS = [int(input()) for _ in range(N)]
