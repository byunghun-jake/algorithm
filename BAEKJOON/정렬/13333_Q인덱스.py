# 5
# 10 8 5 4 3
# 1  2 3 4 5

# 6
# 12 10 9 8 7 5
# 1  2  3 4 5 6

# k개 이상의 논문이 k번 이상 인용되었을 때

# 논문 인용 횟수 중 최대 인용횟수 + 1의 길이를 갖는 count 배열을 생성한다.
# 논문 인용 횟수를 count 배열에 저장한다.
# 역순으로 count 배열을 순환하여 누적한다.
    # 해당 index와 누적 값을 비교하여 누적 값 >= index인 경우
    # 더 작은 값을 q-index로 설정한다.

# def selectionSort(arr):
#     for i in range(N - 1):
#         max_idx = i
#         for j in range(i, N):
#             if arr[max_idx] < arr[j]:
#                 max_idx = j
#         else:
#             arr[i], arr[max_idx] = arr[max_idx], arr[i]
#
#
# N = int(input())
# CITATIONS = list(map(int, input().split()))
# selectionSort(CITATIONS)
# max_citation_count = CITATIONS[0]
# counts = [0] * (max_citation_count + 1)
#
# for c in CITATIONS:
#     counts[c] += 1
#
# q_idx = max_citation_count
# for i in range(max_citation_count - 1, 0, -1):
#     counts[i] += counts[i + 1]
#     if counts[i] >= i:
#         q_idx = min(counts[i], i)
#         break
#
#
# # print(counts)
# print(q_idx)

T = int(input())
arr = list(map(int,input().strip().split()))
arr.sort()
arr.reverse()

idx = 0
while idx < len(arr):
    print(arr[idx], idx)
    if arr[idx] <= idx:
        break
    idx += 1
print(idx)