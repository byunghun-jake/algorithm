import sys

sys.stdin = open("./input.txt")

f = open("./result.txt", "w")

T = int(input())

for test_case in range(1, T + 1):
    test_case_length = int(input())
    building_list = list(map(int, input().split()))
    count = 0
    # TODO: 1. 모든 동을 순환한다. 좌우 2칸에 있는 건물의 높이를 비교한다.

    for i in range(2, test_case_length - 2):
        building_height = building_list[i]
        around_max_height = 0
        for j in range(i - 2, i + 3):
            if j != i and around_max_height < building_list[j]:
                around_max_height = building_list[j]
        if building_height <= around_max_height:
            continue

        count += building_height - around_max_height

    print(f"#{test_case} {count}")
    f.write(f"#{test_case} {count}\n")
