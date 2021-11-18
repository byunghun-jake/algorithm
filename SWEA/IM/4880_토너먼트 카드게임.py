def divide_q(_cards):
    if len(_cards) == 1:
        return _cards[0]
    if len(_cards) == 2:
        a = _cards[0]
        b = _cards[1]
        if a[1] == b[1]:
            return a
        elif a[1] - b[1] == -1 or a[1] - b[1] == 2:
            return b
        else:
            return a

    mid = len(_cards) // 2 + len(_cards) % 2
    left = divide_q(_cards[:mid])
    right = divide_q(_cards[mid:])
    return divide_q([left] + [right])


T = int(input())

for _ in range(T):
    # N: 학생 수
    N = int(input())
    # 시작 인덱스: 1
    cards = list(map(int, input().split()))

    answer = divide_q(list(enumerate(cards)))
    print(answer[0] + 1)
