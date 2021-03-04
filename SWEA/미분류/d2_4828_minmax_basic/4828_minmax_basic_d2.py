import sys

sys.stdin = open("./input.txt")
f = open("./result.txt", "w")

T = int(input())

for test_case in range(1, T+1):
    test_length = int(input())
    number_list = list(map(int, input().split()))

    min_number = number_list[0]
    max_number = number_list[0]

    for idx in range(len(number_list)):
        if number_list[idx] < min_number:
            min_number = number_list[idx]
        elif number_list[idx] > max_number:
            max_number = number_list[idx]

    gap = max_number - min_number
    print(f"#{test_case} {gap}")
    f.write(f"#{test_case} {gap}\n")
