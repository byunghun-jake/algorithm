# 최대로 갈 수 있는 만큼 이동한다.
# 충전기가 있으면 충전한다.
# 충전기가 없다면, 뒤로 이동하여 충전한다.
# 이전 위치로 돌아왔다면, 더 이상 갈 수 없는 것이므로 종료한다.

T = int(input())

for tc in range(1, T + 1):
    # K: 갈 수 있는 거리
    # N: 정류장의 수 (0 ~ N)
    # M: 충전기가 설치된 정류장의 수
    K, N, M = map(int, input().split())
    charges = list(map(int, input().split()))

    current = 0
    count = 0
    while current < N:
        next_stop = current + K
        if next_stop >= N:
            print(f"#{tc} {count}")
            break
        while next_stop > current:
            if next_stop in charges:
                current = next_stop
                count += 1
                break
            else:
                next_stop -= 1
        else:
            print(f"#{tc} 0")
            break