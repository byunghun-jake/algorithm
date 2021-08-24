# 두 인덱스에 있는 값을 교환을 했을 때, 교환을 하지 않았을 때로 구분하여 생각

T = int(input())


for tc in range(1, T + 1):
    origin_num, change_count = map(int, input().split())
    num_list = [int(x) for x in str(origin_num)]
    N = len(num_list)

    change = 0
    i = 0
    change_idx_list = [[] for _ in range(10)]
    change_num_list = [[] for _ in range(10)]
    while change < change_count and i < N:
        idx = i
        num = num_list[i]
        # i + 1번째 인덱스 부터 N - 1번째 인덱스까지의 수 중 i번째 인덱스보다 크면서 가장 큰 수를 찾기
        for j in range(i + 1, N):
            if num <= num_list[j]:
                idx = j
                num = num_list[j]
        if i != idx:
            # 두 값을 교환
            num_list[i], num_list[idx] = num_list[idx], num_list[i]
            change += 1
            change_idx_list[num_list[i]].append(idx)
            change_num_list[num_list[i]].append(num_list[idx])
        i += 1

    duplicated = False
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if num_list[i] == num_list[j]:
                duplicated = True
    if (change_count - change) % 2 == 1 and not duplicated:
        # 남은 교환 횟수가 홀수이고, 동일한 숫자가 없다면 반드시 변경해주어야 한다.
        # 값이 가장 적게 변하려면, 가장 작은 자리수 두 수를 교환
        num_list[-1], num_list[-2] = num_list[-2], num_list[-1]
    # 남은 교환 횟수가 없다면?
    else:
        # 같은 숫자와 교환했다면, 교환한 숫자끼리 정렬한다.
        # 가장 높은 자리수가 큰 수가 되도록
        for i in range(10):
            if len(change_idx_list[i]) > 1:
                change_idx_list[i].sort()
                change_num_list[i].sort(reverse=True)
                for idx in range(len(change_num_list[i])):
                    num_list[change_idx_list[i][idx]] = change_num_list[i][idx]

    print(f"#{tc} {''.join(map(str, num_list))}")

