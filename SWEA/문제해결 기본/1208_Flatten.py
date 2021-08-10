# 높이를 세어서 배열에 저장한다.
# 가장 낮은 높이와 가장 높은 높이를 구한다.
# 덤프를 수행한다.
    # 가장 낮은 높이의 개수를 1 줄이고, +1 높이의 개수를 1 증가시킨다.
    # 가장 높은 높이의 개수를 1 줄이고, -1 높이의 개수를 1 증가시킨다.
# 가장 낮은 높이와 가장 높은 높이를 구한다.
# 덤프를 수행한다.
    # ...

for tc in range(1, 11):
    dump_count = int(input())
    height_list = list(map(int, input().split()))

    height_count_list = [0] * 101
    for height in height_list:
        height_count_list[height] += 1

    min_height = 0
    max_height = 0
    for i in range(101):
        if height_count_list[i]:
            min_height = i
            break
    for i in range(100, 0, -1):
        if height_count_list[i]:
            max_height = i
            break

    while dump_count:
        dump_count -= 1
        height_count_list[max_height] -= 1
        height_count_list[max_height - 1] += 1
        height_count_list[min_height] -= 1
        if min_height == 100:
            print(min_height)
        height_count_list[min_height + 1] += 1

        if height_count_list[max_height] == 0:
            max_height -= 1
        if height_count_list[min_height] == 0:
            min_height += 1

    print(f"#{tc} {max_height - min_height}")