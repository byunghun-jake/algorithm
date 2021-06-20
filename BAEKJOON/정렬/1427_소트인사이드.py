# 배열을 정렬하는 것은 쉽지만, 숫자의 자리수는 어떻게 정렬할 수 있을까?
# 입력받는 숫자를 숫자형으로 보지 않고, 문자형으로 다룬 후에 바로 배열에 넣어보자.

# 각 자리수의 숫자는 0 ~ 9의 숫자이기에, 카운팅정렬에 적합하다고 생각이 들었다.

# strip()을 쓰지 않으면, \n 개행 문자열도 그대로 입력이 되는 걸 확인할 수 있다.


import sys

NUM_ARR = list(map(int, sys.stdin.readline().strip()))
count_arr = [0] * 10

for i in range(len(NUM_ARR)):
    count_arr[NUM_ARR[i]] += 1

result = []
for i in range(9, -1, -1):
    count = count_arr[i]
    for _ in range(count):
        result.append(f"{i}")

print("".join(result))
