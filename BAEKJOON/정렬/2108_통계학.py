# N: 500,000 => O(nlogn)
# 정수의 절댓값은 4000을 넘지 않는다.
# -4000 ~ 4000 => 0 ~ 8000 (최대 크기 8001)

# 카운팅 정렬
# 전달받는 숫자에 4000을 더해준다.
import sys
#################################
def cnt_sort():
    cnt_array = [0] * (NMAX + 1)
    result = []
    # 무작위로 들어온 것들을 하나씩 세본다.
    for i in nums:
        cnt_array[i] += 1

    # 작은 것부터 꺼낸다.
    for i in range(NMAX + 1):
        # i == 1일 때,
        # cnt_array[i] == 2
        for j in range(cnt_array[i]):
            result.append(i)
    return result


N = int(input())
NMAX = 2000
nums = []
# [1, 2, 3, 4]

for i in range(N):
    # 0이상의 수로 만들기 위해
    nums.append(int(input()) + 1000)

for i in cnt_sort():
    print(i - 1000)


#################################
def cnt_sort():
    cnt_array = [0] * (NMAX + 1)
    # [0, 0, 0, 0, 0, 0]
    for i in nums:
        cnt_array[i] += 1
    # [0, 1, 1, 1, 1, 1]
    for l in range(NMAX):
        cnt_array[l + 1] += cnt_array[l]
    # [0, 1, 2, 3, 4, 5]
    result_array = [-1] * N
    # [-1, -1, -1, -1, -1]
    for k in nums: # nums, k = 0~4
        cnt_array[k] -= 1
        result_array[cnt_array[k]] = k
    # [ ]
    return result_array

# N: 숫자의 개수
# 이 수는 절댓값이 1,000보다 작거나 같은 정수
# -1000 ~ 1000
# 0 ~ 2000
# NMAX: 숫자의 최대값 (1000씩 더했을 때)
N = int(input())
NMAX = 2000
nums = []
# [1, 2, 3, 4]

for i in range(N):
    # 0이상의 수로 만들기 위해
    nums.append(int(input()) + 1000)

# [1001, 1002, 1003, 1004]
for i in cnt_sort():
    print(i-1000)

###########################################
N = int(sys.stdin.readline())
NMAX = 8001
count_arr = [0] * NMAX
max_count = 0
for _ in range(N):
    num = int(sys.stdin.readline()) + 4000
    count_arr[num] += 1
    if max_count < count_arr[num]:
        max_count = count_arr[num]

sorted_arr = []
many_arr = []
max_value = 0

for i in range(NMAX):
    count = count_arr[i]
    # 최빈값 찾기
    if count == max_count:
        many_arr.append(i - 4000)
    # 정렬값 넣기
    for _ in range(count):
        sorted_arr.append(i - 4000)
        max_value += i - 4000

# print(sorted_arr)
mean_value = round(max_value / N)
mid_value = sorted_arr[N // 2]
if len(many_arr) > 1:
    many_value = many_arr[1]
else:
    many_value = many_arr[0]
range_value = sorted_arr[-1] - sorted_arr[0]

result = [mean_value, mid_value, many_value, range_value]
for i in range(4):
    print(result[i])


