# 출발점에서 도착점까지의 거리 구하기

import sys

sys.stdin = open("Ladder2.txt")


N = 100
for _ in range(10):
    tc = int(input())
    ladder = []
    cc_list = []

    for idx in range(N):
        ladder.append(list(map(int, input().split())))
        if idx == 0:
            for c in range(N):
                if ladder[idx][c] == 1:
                    cc_list.append(c)


    min_count = 987654321
    answer = 0
    for idx in range(len(cc_list)):
        cc = cc_list[idx]
        cr = 0
        count = 0
        while cr != 99:
            dc = 0
            if cc > 0 and ladder[cr][cc - 1] == 1:
                dc = -1
            elif cc < 99 and ladder[cr][cc + 1] == 1:
                dc = 1

            if dc:
                while 0 <= cc + dc <= 99 and ladder[cr][cc + dc] == 1:
                    cc += dc
                    count += 1
            cr += 1
            count += 1
        if count < min_count:
            min_count = count
            answer = cc_list[idx]
    print(f"#{tc} {answer}")
