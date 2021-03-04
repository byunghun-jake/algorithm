import sys

sys.stdin = open("./input.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    bus_stop = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())

        for j in range(A, B + 1):
            bus_stop[j] += 1

    print(f"#{test_case}", end=" ")
    # 출력할 버스 정류장 입력받기
    bus_stop_count = int(input())

    for stop in range(bus_stop_count):
        stop_index = int(input())

        print(bus_stop[stop_index], end=" ")
