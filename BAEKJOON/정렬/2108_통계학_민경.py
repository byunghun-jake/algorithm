import sys

T = int(sys.stdin.readline())

# 5
# 0
# 0
# 0
# 2
# 2
# cnt = [0, 0, 0, 0, 0]
cnt = [0] * 8001
for i in range(T):
    num = int(sys.stdin.readline())
    cnt[int(num)] += 1

arr = []
max_count = 0

for i in range(-4000, 4000):
    if cnt[i] >= 1:
        for j in range(cnt[i]):
            arr.append(i)
    if cnt[i] > max_count:
        max_count = cnt[i]

same = []
max_v = 0
for i in range(-4000, 4000):
    if cnt[i] == max_count:
        same.append(i)
if len(same) > 1:
    max_v = same[1]
else:
    max_v = same[0]

sum_v = 0
for i in range(len(arr)):
    sum_v += arr[i]

avg = round(sum_v / len(arr))
middle = arr[len(arr) // 2]
range_v = arr[-1] - arr[0]

print(avg, middle, max_v, range_v, sep='\n')