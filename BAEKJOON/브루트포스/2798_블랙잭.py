# N: 카드의 개수
# M: 최대 값
N, M = map(int, input().split())
# cards: 카드에 쓰여진 수 배열
cards = list(map(int, input().split()))
n = len(cards)

# 모든 부분집합을 구하며, 부분집합의 합이 M을 넘지않는 가장 큰 수를 찾기
result = 0
total = 0
is_done = False
for a in range(n-2):
    for b in range(a+1, n-1):
        for c in range(b+1, n):
            total = cards[a] + cards[b] + cards[c]
            if total == M:
                result = M
                is_done = True
                break
            if result < total < M:
                result = total
        if is_done:
            break
    if is_done:
        break

print(result)
for i in range(1 << n):
    sub_cards = []
    for j in range(n):
        if i & (1 << j):
            sub_cards.append(cards[j])
            if len(sub_cards) > 3 and sum(sub_cards) > M:
                break
    if len(sub_cards) == 3:
        total = sum(sub_cards)
        if total == M:
            result = total
            break
        elif result < total <= M:
            result = total
print(result)


















