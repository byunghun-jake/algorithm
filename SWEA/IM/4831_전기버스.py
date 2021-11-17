# K: 한 번에 이동할 수 있는 정류장 수
# N: 목적지
# M: 충전기가 설치된 정류장 수
# charger_list: 충전기가 설치된 정류장

T = int(input())
for _ in range(T):
    answer = 0
    K, N, M = map(int, input().split())
    charger_list = list(map(int, input().split()))
    start_point = 0
    bus_stack = []
    count = 0
    for i in range(1, 1 + K):
        bus_stack.append(i)

    while bus_stack:
        current_pos = bus_stack[-1]
        if current_pos >= N:
            answer = count
            break
        if charger_list.count(current_pos) == 1:
            bus_stack = []
            for i in range(current_pos + 1, current_pos + 1 + K):
                bus_stack.append(i)
            count += 1
            continue
        bus_stack.pop()

    print(answer)