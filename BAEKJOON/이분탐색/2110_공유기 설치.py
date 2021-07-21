# 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치

# 1 2  4    8 9

# 조건이 뭘까
    # 간격!

# N, C = map(int, input().split())
# ROUTERS = sorted(int(input()) for _ in range(N))
#
# min_gap = 1
# max_gap = max(ROUTERS) - min(ROUTERS)
#
# while min_gap <= max_gap:
#     gap = (max_gap + min_gap) // 2
#
#     # gap만큼 띄어가면서 공유기를 C개만큼 설치할 수 있는지 확인
#     before_router_x = ROUTERS[0]
#     count = 1
#     for i in range(1, N):
#         distance = ROUTERS[i] - before_router_x
#         if distance >= gap:
#             count += 1
#             before_router_x = ROUTERS[i]
#
#     # 설치 결과
#     if count >= C:
#         min_gap = gap + 1
#     else:
#         max_gap = gap - 1
#
# print(max_gap)
#
#


# N: 집의 개수
# C: 공유기의 개수
N, C = map(int, input().split())
Houses = [int(input()) for _ in range(N)]
Houses.sort()

min_gap = 0
max_gap = Houses[-1]

while min_gap <= max_gap:
    gap = (max_gap + min_gap) // 2
    prev_position = Houses[0]
    # 0번째 집은 공유기를 설치하고 시작한다.
    router_count = C - 1
    # 2번째 집부터 공유기를 설치한다.
    for house_idx in range(1, N):
        # gap보다 크거나 같은 집에 설치한다.
        if Houses[house_idx] - prev_position >= gap:
            router_count -= 1
            prev_position = Houses[house_idx]
        if router_count == 0:
            break
    if router_count == 0:
        min_gap = gap + 1
    else:
        max_gap = gap - 1
print(max_gap)
























