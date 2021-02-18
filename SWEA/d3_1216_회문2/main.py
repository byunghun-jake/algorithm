# start 지점과 end 지점을 만들고,
# start는 고정한 상태에서 end를 start 지점까지 끌고 온다.

# start < end 조건이 성립하지 않거나, 지금까지 찾은 palindrome 길이보다 작다면 다음 단계로 넘어간다.

# 시간이 너무 오래걸려서 스킵하는 조건을 넣는다.
# s - e 사이 거리가 L보다 작다면, 스킵

# 1. 행 단위로 탐색
# 1-1. 열을 가지고, start/end 에 대한 반복문 수행
import sys

sys.stdin = open("input.txt")


def check_pelindrome(t):
    start = 0
    end = len(t)-1
    while start < end:
        if t[start] != t[end]:
            return 0
        start += 1
        end -= 1
    else:
        return len(t)

N = 100

for _ in range(1, 11):
    tc = int(input())

    # arr: 문자열
    arr = [list(input()) for _ in range(N)]

    start = 0
    end = N-1
    # L: pelindrome의 최대 길이
    L = 1

    # 행 단위로 탐색
    for r in range(N):
        # 시작 지점과 끝 지점을 가지고 반복
        for s in range(N-1):
            if N-s < L:
                break
            for e in range(N-1, s, -1):
                if e-s < L:
                    break
                # 문자열을 만들면서, 회문임을 확인할 수는 없을까?
                # 아니면, 첫 단어라도 비교해본다면?
                if arr[r][s] != arr[r][e]:
                    continue

                # 문자열 만들기
                text = ""
                for c in range(s, e+1):
                    text += arr[r][c]
                # 회문 찾기
                pelindrome_length = check_pelindrome(text)
                if L < pelindrome_length:
                    L = pelindrome_length

    # 열 단위로 탐색
    for c in range(N):
        # 시작 지점과 끝 지점을 가지고 반복
        for s in range(N-1):
            if N-s < L:
                break
            for e in range(N-1, s, -1):
                if e-s < L:
                    break
                if arr[s][c] != arr[e][c]:
                    continue

                # 문자열 만들기
                text = ""
                for r in range(s, e + 1):
                    text += arr[r][c]
                # 회문 찾기
                pelindrome_length = check_pelindrome(text)
                if L < pelindrome_length:
                    L = pelindrome_length

    print(f"#{tc} {L}")




























