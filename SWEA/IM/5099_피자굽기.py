# 피자를 꺼낸다.
    # 꺼낼 피자의 치즈를 2로 나눈다. // 2
    # 피자의 치즈가 0이라면, 남은 피자가 있는 지 확인하고, 피자를 꺼내 넣는다.
    # 피자의 치즈가 0이 아니라면, 맨 마지막으로 넣는다 list.append()
from collections import deque

T = int(input())

for _ in range(T):
    answer = -1
    # N: 화덕의 크기
    # M: 피자의 개수
    N, M = map(int, input().split())
    oven = deque()
    pizza_data = list(map(int, input().split()))
    pizza_list = deque([])
    for i in range(M):
        pizza_list.append([i + 1, pizza_data[i]])

    # 피자를 넣는다.
    for _ in range(N):
        pizza = pizza_list.popleft()
        oven.append(pizza)

    # 피자를 확인한다.
    while oven:
        print(oven)
        # 피자를 꺼낸다
        pizza = oven.popleft()
        pizza[1] = pizza[1] // 2

        if pizza[1] == 0:
            answer = pizza[0]
            if pizza_list:
                new_pizza = pizza_list.popleft()
                oven.append(new_pizza)
        else:
            oven.append(pizza)

    print(answer)