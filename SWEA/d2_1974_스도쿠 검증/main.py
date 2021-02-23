import sys

sys.stdin = open("input.txt")

# T: 테스트 케이스 개수
T = int(input())

for tc in range(1, T+1):
    # 퍼즐 입력받기
    puzzle = [list(map(int, input().split())) for _ in range(9)]

    result = 1

    # 행 단위 검사
    for r in range(9):
        r_num_list = [0] * 10
        c_num_list = [0] * 10
        for c in range(9):
            if r_num_list[puzzle[r][c]] == 1 or c_num_list[puzzle[c][r]] == 1:
                result = 0
            else:
                r_num_list[puzzle[r][c]] += 1
                c_num_list[puzzle[c][r]] += 1
        if result == 0:
            break

    # 3x3 단위 검사
    if result == 1:
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if result == 1:
                    num_list = [0] * 10
                    for r in range(3):
                        for c in range(3):
                            if num_list[puzzle[i+r][i+c]] == 1:
                                result = 0
                                break
                            else:
                                num_list[puzzle[i + r][i + c]] += 1

    print(f"#{tc} {result}")






















