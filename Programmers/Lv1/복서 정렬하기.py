def solution(weights, head2head):
    answer = []
    N = len(weights)
    index = [i for i in range(1, N + 1)]
    # 1. 승률을 기준으로 내림차순 정렬
    # 2. 승률이 동일한 경우: 자신보다 몸무게가 무거운 복서를 이긴 횟수 기준으로 내림차순
    # 3. 이긴 횟수가 동일한 경우: 자신의 몸무게를 기준으로 내림차순
    # 4. 몸무게가 동일한 경우: 번호를 기준으로 오름차순
    winningrate_list = [0 for _ in range(N)]
    heavywin_list = [0 for _ in range(N)]
    for i in range(N):
        h = head2head[i]
        count = 0
        win = 0
        heavywin = 0
        for j in range(N):
            res = h[j]
            if res == "N":
                continue
            elif res == "W":
                win += 1
                count += 1
                if weights[i] < weights[j]:
                    heavywin += 1
            elif res == "L":
                count += 1
        if count == 0:
            winningrate_list[i] = 0
        else:
            winningrate_list[i] = (win / count)
        heavywin_list[i] = heavywin
    boxer_list = list(zip(winningrate_list, heavywin_list, weights, index))
    boxer_list.sort(key=lambda boxer: (-boxer[0], -boxer[1], -boxer[2], boxer[3]))
    answer = [x[3] for x in boxer_list]
    return answer
a = solution([50, 82, 75, 120], ["NLWL", "WNLL", "LWNW", "WWLN"])
print(a)