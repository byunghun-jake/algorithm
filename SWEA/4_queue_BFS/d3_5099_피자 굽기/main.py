import sys

sys.stdin = open("input.txt")

# N개의 피자를 동시에 구울 수 있는 화덕
# 치즈가 모두 녹으면 화덕에서 꺼내지만, 걸리는 시간은 치즈의 양에 의해 결정되며, 치즈의 양은 피자마다 다르다
# 치즈의 양을 확인하기 위해 꺼낼 때, 녹지 않은 치즈의 양을 줄이면 되겠다

def cook(_pizza_list):
    oven = []
    # oven에 피자 넣기
    for i in range(N):
        oven.append(_pizza_list.pop(0))

    while oven:
        # print(oven)
        # 맨 앞에 있는 피자의 상태 확인
        front = oven.pop(0)
        # 치즈 양 변경
        cheeze = front[0] // 2
        idx = front[1]

        # 치즈가 아직 남아있다면, oven 맨 뒤로 다시 넣어준다.
        if cheeze:
            oven.append((cheeze, idx))
            continue
        # 치즈의 양이 0이라면, oven에서 뺀 상태를 유지한다.
        # 남은 피자가 있다면, 빈 자리에 넣어준다.
        if _pizza_list:
            oven.append(_pizza_list.pop(0))
        # 남은 피자가 없고, oven에 남은 피자가 하나라면 이 피자의 번호를 리턴한다.
        if len(oven) == 1:
            last_pizza = oven.pop(0)
            return last_pizza[1]


TC = int(input())
for tc in range(1, TC + 1):
    # N: oven의 크기
    # M: 피자의 개수
    N, M = map(int, input().split())

    pizza_list = list(map(int, input().split()))
    # 리스트 요소에 인덱스 포함시키기
    for i in range(M):
        pizza_list[i] = (pizza_list[i], i + 1)

    result = cook(pizza_list[:])
    print(f"#{tc} {result}")