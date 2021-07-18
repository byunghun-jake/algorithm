# 특정한 숫자 카드를 몇 개 가지고 있는지 구하는 프로그램

# N = 500,000
# 수의 범위 = -10,000,000 ~ 10,000,000
# M = 500,000

N = int(input())
MY_CARDS = list(map(int, input().split()))
M = int(input())
CARD_NUMS = list(map(int, input().split()))

# 1. 딕셔너리로 풀면 안될까?
# my_cards_dict = {}
# for num in MY_CARDS:
#     if my_cards_dict.get(num):
#         my_cards_dict[num] += 1
#     else:
#         my_cards_dict[num] = 1
#
# result = []
# for num in CARD_NUMS:
#     if my_cards_dict.get(num):
#         result.append(my_cards_dict.get(num))
#     else:
#         result.append(0)
#
# print(*result)

# 2. 이분탐색 풀이
# 정렬한 뒤에 이분 탐색 시행
# 근데, 이분 탐색은 일치하는 거 찾으면 끝나는 건데
# 일치하는 거 찾은 뒤에 바로 앞, 뒤에 동일한 숫자가 있는지 확인해야 할까?
def merge(left, right):
    result = []
    l_idx = r_idx = 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1
    if l_idx < len(left):
        result += left[l_idx:]
    else:
        result += right[r_idx:]
    return result


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


# 정렬한 카드를 앞에서 부터 읽으면서, 개수를 저장한다.
count_store_dict = {}
for num in MY_CARDS:
    if count_store_dict.get(num):
        count_store_dict[num] += 1
    else:
        count_store_dict[num] = 1

# 중복 제거
# set_MY_CARDS = list(set(MY_CARDS))
# set_length = len(set_MY_CARDS)

# 정렬
sorted_MY_CARDS = merge_sort(MY_CARDS)

result = []

# 이분탐색
def binary_search(s, e, target_num):
    if s > e:
        result.append(0)
        return

    mid = (s + e) // 2
    if sorted_MY_CARDS[mid] == target_num:
        result.append(count_store_dict[target_num])
    elif sorted_MY_CARDS[mid] > target_num:
        binary_search(s, mid - 1, target_num)
    else:
        binary_search(mid + 1, e, target_num)

for num in CARD_NUMS:
    binary_search(0, N - 1, num)

print(*result)