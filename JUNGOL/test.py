# # 2칸 이동 or 7칸 이동
#
# # 1. 2칸 이동했을 때
#     # 2칸 이동 or 7칸 이동
# # 2. 7칸 이동했을 때
#     # 2칸 이동 or 7칸 이동
#
# # 종료 조건
#     # 1. 다음 n이 14를 넘었을 때
#
# # N = 14
# # MAP = 1 50 1 -1 1 3 -5 1 -15 0 100 1 1 2
#
# # def getHighestScore(score, stage):
# #     global highestScore
# #     # 종료 조건
# #     if stage > N:
# #         if score > highestScore:
# #             highestScore = score
# #         return
# #
# #     currentStageScore = MAP[stage]
# #     # 2칸 이동
# #     getHighestScore(score + currentStageScore, stage + 2)
# #     # 7칸 이동
# #     getHighestScore(score + currentStageScore, stage + 7)
# #
# # N = int(input())
# # MAP = [0]
# # MAP += list(map(int, input().split()))
# # highestScore = 0
# # getHighestScore(0, 0)
# # print(highestScore)
#
#
#
# # 뒤에서부터 넘어오는 방법?
# MAP = [0] * 1000
# N = int(input())
# MEMO = [0] * 1000
#
# def getPoint(stage):
#     if stage == 0:
#         return 0
#     if stage < 0:
#         return -999999
#     if MEMO[stage]
#
# temp_map = list(map(int, input().split()))
# for i in range(N):
#     MAP[i + 1] = temp_map[i]
#
# highest_score = -21e8
# for i in range(1, 6):
#     ret = getPoint(N + i)
#     if ret > highest_score:
#         highest_score = ret
#
# print(highest_score)


# 양탄자 문제

# 도착점을 찾는다.
# 도착점에서 시작하여 각 칸별로 최소 거리를 저장하며 나아가는 방식
# 갈 수 있는 칸을 확인한다.
    # 요술램프가 있는지?
    # Index를 초과하는지?
    # 벽으로 막혀있는지?
    # 방문한 적이 있는지?
# 다음에 이동할 칸에 값이 있는지 확인한다.
    # 값이 있다면?
        # 현재 칸에서 1 더한 값보다 값이 크다면 값을 교체한다.
    # 값이 없다면?
        # 현재 칸에서 1 더한 값을 입력한다.























