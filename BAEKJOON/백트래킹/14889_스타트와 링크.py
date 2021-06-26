# N명 / 짝수
# N / 2명으로 나눈 두 개의 팀
# 두 팀 시너지 합의 차이가 최소가 되려면?
# 지금까지 구했던 시너지 차이 중 최소 값을 저장해두고, 그 값보다 시너지가 크다면 더이상 진행하지 않는 방법
# 그럼 결국 다 구해야 하는 거 아닌가?
# 가지치기 없이 기본적인 탐색을 먼저 구현해보자

# 팀 구성하기
# 순회하며, 두 배열에 팀원을 담는다.
# 모든 팀원을 순회했다면, 팀 구성은 종료

N = int(input())
BOARD = [list(map(int, input().split())) for _ in range(N)]

# 뽑은 맴버를 저장하는 배열
sel = [0] * (N // 2)
# 맴버가 뽑혔는지 저장하는 배열
check = [0] * N

teams = []

def make_team(idx, start_num):
    if idx == (N // 2):
        teams.append(sel[:])
        return

    for i in range(start_num, N):
        # 이미 뽑혔다면 패스
        if check[i]: continue
        # i 맴버를 뽑기
        sel[idx] = i
        check[i] = 1
        make_team(idx + 1, i)
        # 뽑기 취소
        check[i] = 0


def calc_synergy(team):
    synergy = 0
    for i in team:
        for j in team:
            synergy += BOARD[i][j]
    return synergy

make_team(0, 0)
# print(teams)
synergy_list = []
# 양 끝에 있는 값끼리 시너지를 구한 뒤 최소 시너지를 찾는다.
for team in teams:
    synergy_list.append(calc_synergy(team))

# print(synergy_list)
min_synergy_gap = max(synergy_list)
L = len(synergy_list)
for i in range(L // 2):
    min_synergy_gap = min(min_synergy_gap, abs(synergy_list[i] - synergy_list[L - i - 1]))
print(min_synergy_gap)
