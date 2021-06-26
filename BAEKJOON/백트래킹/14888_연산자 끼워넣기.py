# 음수 나눗셈 방식은 파이썬의 // 연산자를 그대로 쓰면 안된다.
# -3 // 2 = -2가 나오는데, 이 문제 기준으로는 -1이 나와야 한다.

# 1단계
# 수를 하나씩 넣어보고, 최소값과 최대값을 구해보자

def checkValue(value):
    global min_value, max_value
    min_value = min(min_value, value)
    max_value = max(max_value, value)


def calculator(n_idx = 1, value = 0):
    if n_idx == N:
        # print(value)
        checkValue(value)
        return

    for op_idx in range(4):
        # 연산자를 쓸 수 없다면 다음 연산자 확인
        if OPERATORS[op_idx] == 0: continue

        # 연산자를 쓸 수 있다면
        # 나눗셈이라면
        OPERATORS[op_idx] -= 1
        new_num = 0
        if op_idx == 3:
            if value < 0:
                new_num = -(abs(value) // NUMS[n_idx])
            else:
                new_num = value // NUMS[n_idx]
        elif op_idx == 0:
            new_num = value + NUMS[n_idx]
        elif op_idx == 1:
            new_num = value - NUMS[n_idx]
        else:
            new_num = value * NUMS[n_idx]
        calculator(n_idx + 1, new_num)

        # 연산자 사용 취소
        OPERATORS[op_idx] += 1





N = int(input())
NUMS = list(map(int, input().split()))
OPERATORS = list(map(int, input().split()))

min_value = 9876543210
max_value = -9876543210

calculator(1, NUMS[0])
print(max_value)
print(min_value)
