# 1. 내 위치
# 2. 최대 갈 수 있는 위치
# 3. 목적지에 도착 했는가?
# 4. 도착했다면, 종료
# 5. 도착하지 못했다면, 내 위치(<)와 최대 갈 수 있는 위치(>=) 사이에 충전소가 있는지 확인
# 6. 충전소가 있다면, 가장 먼 충전소로 내 위치를 이동하고 충전 횟수 1 추가
# 7. 충전소가 없다면, 충전 횟수를 0으로 변환 후 종료

import sys

sys.stdin = open("./input.txt")

T = int(input())
for test_case in range(1, T + 1):
    step, destination, bus_stop_length = list(map(int, input().split()))
    bus_stop_list = list(map(int, input().split()))
    current_position = 0
    charge_count = 0

    while current_position < destination:
        next_position = current_position + step

        if next_position >= destination:
            break

        next_bus_stop = 0
        for bus_stop in bus_stop_list:
            if current_position < bus_stop <= next_position:
                next_bus_stop = bus_stop

        if not next_bus_stop:
            charge_count = 0
            break
        else:
            current_position = next_bus_stop
            charge_count += 1

    print(f"#{test_case} {charge_count}")
