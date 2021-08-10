# 조망권을 확인하는 건물의 인덱스가 i일 때,
# i-2, i-1, i+1, i+2 중 가장 높은 건물을 찾아 i와 비교한다.
# i가 더 낮다면 조망권은 확보가 되지 않고, i가 더 높다면 높은 만큼의 층은 조망권이 확보가 된다.

for tc in range(1, 11):
    N = int(input())
    B = list(map(int, input().split()))

    answer = 0

    for i in range(2, N - 2):
        near_building_height = max(B[i-2], B[i-1], B[i+1], B[i+2])
        if B[i] <= near_building_height:
            continue
        else:
            answer += B[i] - near_building_height

    print(f"#{tc} {answer}")