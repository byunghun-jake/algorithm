# 1. 0~9까지 카운팅 리스트를 만든다.
# 2. while 반복문을 사용한다. (곱할 값을 0으로 초기화한다.)
# 2-1. 주어진 값에 곱할 값을 곱한다.
# 2-2. 자리수에 담긴 숫자를 이용해, 카운팅 리스트에 담는다.
# 2-3. 카운팅 리스트의 각 인덱스에 빠짐없이 모든 값이 담겼는지 확인한다.

import sys

sys.stdin = open("./input.txt")


def get_digits(number):
    return_digits = []
    while number != 0:
        return_digits.append(number % 10)
        number = number // 10
    return return_digits


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    count = 0
    digit_counter = [0] * 10

    while True:
        count += 1
        temp = N * count
        digits = get_digits(temp)

        for digit in digits:
            digit_counter[digit] += 1

        for counter in digit_counter:
            if counter == 0:
                break
        else:
            break
    print(f"#{test_case} {count * N}")
