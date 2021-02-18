import sys

sys.stdin = open("input.txt")


def check_palindrome(t):
    # 양 끝부터 탐색
    start = 0
    end = len(t) - 1
    # 시작지점이 끝지점과 같아지거나 넘어갈 때 까지 반복
    while start < end:
        # 양 끝의 문자가 서로 다르다면, False를 리턴
        if t[start] != t[end]:
            return False
        start += 1
        end -= 1
    else:
        return True


T = int(input())
for tc in range(1, T+1):
    # N: 배열 크기
    # M: 회문 길이
    N, M = map(int, input().split())

    # 배열을 입력받는다
    arr = [list(input()) for _ in range(N)]

    # print(arr)
    # 10x10인 배열에서는 (0,0)~(0,9) / (0,0)~(9,0)만 검사하면 되겠다
    find_palindrome = None
    # -> 방향(행)으로 검사
    # 모든 행에 대해
    for r in range(N):
        # s: 회문 검사 시작 지점
        for s in range(0, N-M+1):
            text = ""
            for c in range(s, s+M):
                text += arr[r][c]
            # 회문 검사
            if check_palindrome(text):
                find_palindrome = text
                break
        # 회문을 찾았다면, 반복문을 나감
        if find_palindrome:
            break

    # 회문을 못 찾았다면, 다음 검사 진행
    if not find_palindrome:
        # 모든 열에 대해 검사
        for c in range(N):
            for s in range(0, N-M+1):
                text = ""
                for r in range(s, s+M):
                    text += arr[r][c]
                # 회문 검사
                if check_palindrome(text):
                    find_palindrome = text
                    break
            # 회문을 찾았다면, 반복문을 나감
            if find_palindrome:
                break

    print(f"#{tc} {find_palindrome}")

















































