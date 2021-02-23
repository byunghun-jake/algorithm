# 0번째 피보나치 수는 0
# 1번째 피보나치 수는 1
# F(n) = F(n-1) + F(n-2) (n >= 2)
def fibonacci(n):
    # 종료 조건
    if n < 2:
        return n

    # 재귀
    return fibonacci(n-1) + fibonacci(n-2)


N = int(input())
print(fibonacci(N))



























