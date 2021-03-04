# 반으로 나누었을 때, 최소로 쪼개지는 경우는 1명 또는 2명
import sys

sys.stdin = open("input.txt")


def dfs(cards):
    if len(cards) == 1:
        return cards[0]

    if len(cards) == 2:
        card1 = cards[0]
        card2 = cards[1]
        if card1[0] == card2[0]:
            if card1[1] < card2[1]:
                return card1
            else:
                return card2
        elif card1[0] - card2[0] == -1 or card1[0] - card2[0] == 2:
            return card2
        else:
            return card1

    mid_idx = len(cards) // 2 + len(cards) % 2
    cards_a = cards[:mid_idx]
    cards_b = cards[mid_idx:]
    # 반을 나눈 후 각각의 승자를 구한다 => dfs(cards_a) & dfs(cards_b)
    # 각각의 승자를 합쳐 승자를 구한다 => dfs([dfs(cards_a)] + [dfs(cards_b)])
    return dfs([dfs(cards_a)] + [dfs(cards_b)])


TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    CARD_LIST = list(map(int, input().split()))
    for i in range(N):
        CARD_LIST[i] = (CARD_LIST[i], i + 1)

    result = dfs(CARD_LIST)[1]
    print(f"#{tc} {result}")