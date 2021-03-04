import sys

sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    # 버스노선 갯수 및 다닐 수 있는 노선
    N = int(input())
    A = [0] * N
    B = [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())

    # 버스정류장 갯수
    P = int(input())

    C = [0] * P
    for i in range(P):
        C[i] = int(input())

    counts = [0] * P

    for i in range(N):
        for j in range(P):
            if A[i] <= C[j] <= B[i]:
                counts[j] += 1

    # 출력 형식을 맞추기
    result = ""
    for count in counts:
        result += str(count)
    result = " ".join(result)

    print("#{} {}".format(tc, result))