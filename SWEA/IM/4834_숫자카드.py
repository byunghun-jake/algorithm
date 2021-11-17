T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    num_list = list(map(int, input().split()))

    sub_sum_num_list = [sum(num_list[:M])]

    for i in range(1, N - M + 1):
        sub_sum_num_list.append(sum(num_list[i:i + M]))

    print(max(sub_sum_num_list), min(sub_sum_num_list))
    print(max(sub_sum_num_list) - min(sub_sum_num_list))