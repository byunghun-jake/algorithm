# N!을 출력하는 프로그램을 작성하시오

N = int(input())


def factorial(n):
    # 종료 조건
    if n == 0:
        return 1

    # 변화 조건
    return n * factorial(n-1)


print(factorial(N))


























