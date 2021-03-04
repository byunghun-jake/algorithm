import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    c = [0] * 12    # 0 ~ 9 & (i+1), (i+2)
    NUM = int(input())

    for _ in range(6):
        c[NUM % 10] += 1
        NUM //= 10

    t = r = 0   # 초기화
    i = 0           # for문은 동일한 인덱스에서 같은 동작을 수행하기 어렵다.
    while i < 10:
        # 트리플 찾기
        if c[i] >= 3:
            t += 1
            c[i] -= 3
            continue
        if c[i] > 0 and c[i+1] > 0 and c[i+2] > 0:
            r += 1
            c[i] -= 1
            c[i+1] -= 1
            c[i+2] -= 1
            continue
        i += 1

    if r + t == 2:
        print(f"#{tc} Baby Gin")
    else:
        print(f"#{tc} Lose")



































