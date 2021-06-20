# N: 500,000 => O(nlogn)
# 정수의 절댓값은 4000을 넘지 않는다.
# -4000 ~ 4000 => 0 ~ 8000 (최대 크기 8001)

# 카운팅 정렬
# 전달받는 숫자에 4000을 더해준다.
import sys

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


