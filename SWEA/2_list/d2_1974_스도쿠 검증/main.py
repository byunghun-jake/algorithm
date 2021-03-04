import sys

sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    # 스도쿠 퍼즐의 크기는 9 x 9
    # 검사 순서
    # 1. 행 우선 탐색
    # 2. 열 우선 탐색
    # 3. 3 x 3 탐색
    # sudoku: 스도쿠 저장
    sudoku = [list(map(int, input().split())) for _ in range(9)]

    # result: 결과 (1 or 0)
    result = 1

    # 행 단위로 탐색하기
    r = 0
    c = 0
    while result == 1 and r < 9:
        # check: 1부터 9까지의 번호를 만난 횟수를 저장하는 배열
        check = [0] * 10
        while result == 1 and c < 9:
            num = sudoku[r][c]
            if check[num] == 0:
                check[num] = 1
            elif check[num] == 1:
                result = 0
            c += 1
        c = 0
        r += 1
    r = 0

    # 열 단위로 검색하기
    while result == 1 and c < 9:
        check = [0] * 10
        while result == 1 and r < 9:
            num = sudoku[r][c]
            if check[num] == 0:
                check[num] += 1
            elif check[num] == 1:
                result = 0
            r += 1
        r = 0
        c += 1
    c = 0

    # 3 x 3 단위로 검색하기
    while result == 1 and r < 9:
        while result == 1 and c < 9:
            check = [0] * 10
            for dr in range(3):
                for dc in range(3):
                    num = sudoku[r+dr][c+dc]
                    if check[num] == 0:
                        check[num] += 1
                    else:
                        result = 0
            c += 3
        c = 0
        r += 3
    r = 0

    print(f"#{tc} {result}")












































