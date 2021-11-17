# 내림차 순 정렬 배열과
# 오름차 순 정렬 배열을
# 하나씩 선택해서 결과 배열에 저장한다.
T = int(input())

for _ in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    ascend = sorted(num_list)
    descend = sorted(num_list, reverse=True)

    answer = []
    for i in range(5):
        answer.append(descend[i])
        answer.append(ascend[i])

    print(answer)