# 쇠 막대기의 시작과 끝을 정하고, 다음 레이저가 위치한 곳 까지

import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T + 1):
    line = list(input())
    L = len(line)
    # 회문처럼 풀어볼까?

    line_list = []
    laser_list = []

    # 시작점 설정
    start = 0
    result = 0
    while start < L - 1:
        # 종료점 설정
        # 시작점 바로 옆부터 커지면서 (는 +1 )는 -1이 되고,
        # 0이 되는 순간 판단 종료
        # 0이 되지 않은 상태로 끝까지 도달해도 종료
        if line[start] == ")":
            continue

        for e in range(start + 1, L):
            if line[e] == "(":
                continue
            count = 1
            pipe_count = 1
            sub_line = line[start:e + 1]
            before_col = "("
            for i in range(1, len(sub_line)):
                if sub_line[i] == "(":
                    count += 1
                else:
                    count -= 1
                    if count == 0:
                        break
            if count == 0:
                if e - start == 1:
                    laser_list.append(start)
                else:
                    # line_list.append((s, e))
                    result += pipe_count
                    break
        start += 1


    # print(line_list)
    # print(laser_list)

    # 파이프 리스트를 순환하며 몇 개의 파이프가 나오는지 확인
    # count = 0
    # for s, e in line_list:
    #     count += 1
    #     for i in range(s, e):
    #         for laser_point in laser_list:
    #             if i == laser_point:
    #                 count += 1
    print(f"#{tc} {pipe_count}")







































