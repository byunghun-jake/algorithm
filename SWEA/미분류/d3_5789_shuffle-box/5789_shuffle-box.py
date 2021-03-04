import sys
sys.stdin = open("./input.txt")

T = int(input())
for test_case in range(1, T + 1):
    box_length, rename_count = map(int, input().split())

    box_list = [0] * box_length

    for i in range(1, rename_count + 1):
        left_index, right_index = map(int, input().split())
        for idx in range(left_index - 1, right_index):
            box_list[idx] = i

    print(f"#{test_case} {' '.join(map(str, box_list))}")
