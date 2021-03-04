# 1. 버스 노선의 개수를 받는다.
# 2. 노선의 개수만큼 순환하여, 노선의 시작지와 종착지를 받는다..
# 3. 출력할 버스 정류장의 개수를 받는다.
# 4. 버스 정류장의 개수 만큼 순환하여, 정류장을 받는다.
# 5. 카운팅 리스트를 만들어, 버스 정류장에 노선이 지나가는 횟수를 카운팅한다.
# 6. 버스 정류장 리스트를 출력한다.

import sys

sys.stdin = open("./input.txt")

T = int(input())
for test_case in range(1, T + 1):
    bus_route_count = int(input())
    bus_route_list = [0] * bus_route_count

    # 2
    for idx in range(bus_route_count):
        bus_route_list[idx] = list(map(int, input().split()))

    # 3
    bus_stop_count = int(input())

    # 4
    bus_stop_list = [0] * bus_stop_count
    for i in range(bus_stop_count):
        bus_stop_list[i] = int(input())

    # 5
    bus_stop_counting_list = [0] * bus_stop_count
    for i in range(bus_route_count):
        bus_start, bus_stop = bus_route_list[i]
        for j in range(bus_start, bus_stop + 1):
            for k in range(bus_stop_count):
                if bus_stop_list[k] == j:
                    bus_stop_counting_list[k] += 1

    print(f"#{test_case} {' '.join(map(str, bus_stop_counting_list))}")
