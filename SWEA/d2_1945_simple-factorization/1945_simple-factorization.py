import sys
sys.stdin = open("./input.txt")

T = int(input())
for test_case in range(1, T + 1):
    a = b = c = d = e = 0
    num = int(input())

    while num % 2 == 0:
        num /= 2
        a += 1

    while num % 3 == 0:
        num /= 3
        b += 1

    while num % 5 == 0:
        num /= 5
        c += 1

    while num % 7 == 0:
        num /= 7
        d += 1

    while num % 11 == 0:
        num /= 11
        e += 1

    print(f"#{test_case} {a} {b} {c} {d} {e}")
