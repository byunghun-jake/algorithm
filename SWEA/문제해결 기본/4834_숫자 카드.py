T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    CARDS = list(map(int, input()))
    counter = [0] * 10
    for card in CARDS:
        counter[card] += 1

    max_card = 0
    max_count = 0
    for idx in range(10):
        if max_count <= counter[idx]:
            max_count = counter[idx]
            max_card = idx

    print(f"#{tc} {max_card} {max_count}")
