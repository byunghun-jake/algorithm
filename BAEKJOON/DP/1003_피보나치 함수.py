# 여러 테스트 케이스를 푸는 문제
# 결과 값을 저장해두고, 참조해서 사용한다.

# N은 40보다 작거나 같은 자연수 또는 0

def fib(n):
    if n == 0:
        count[0] += 1
        return 0
    elif n == 1:
        count[1] += 1
        return 1
    else:
        if fib_store[n - 1] != -1:
            fib_next_1 = fib_store[n - 1]
        else:
            fib_next_1 = fib(n - 1)
            fib_store[n - 1] = fib_next_1
        if fib_store[n - 2] != -1:
            fib_next_2 = fib_store[n - 2]
        else:
            fib_next_2 = fib(n - 2)
            fib_store[n - 2] = fib_next_2

        return fib_next_1 + fib_next_2


TC = int(input())
fib_store = [-1] * 41

for tc in range(TC):
    count = [0, 0]
    N = int(input())
    answer = fib(N)
    fib_store[N] = answer
    print()
