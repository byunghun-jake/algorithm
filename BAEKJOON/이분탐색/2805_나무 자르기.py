# 가능한 최대 값을 구하는 문제
# 가져갈 수 있는 나무의 길이 = 나무의 길이 - 톱의 높이 (단, 나무의 길이 > 톱의 높이)

# N, M = map(int, input().split())
# TREES = list(map(int, input().split()))
#
# min_height = 1
# max_height = max(TREES)
#
# while min_height <= max_height:
#     mid_height = (max_height + min_height) // 2
#
#     # 나무 베기
#     cut_tree_length = sum(TREES)
#     for tree in TREES:
#         if tree <= mid_height:
#             cut_tree_length -= tree
#         cut_tree_length -= mid_height
#
#         if cut_tree_length <= M:
#             break
#     if cut_tree_length >= M:
#         min_height = mid_height + 1
#     else:
#         max_height = mid_height - 1
#
# print(max_height)
#
