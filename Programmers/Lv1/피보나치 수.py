fibo_dict = {
    1: 1,
    2: 1,
    3: 2,
    4: 3
}

def fibo(n):
    n1 = fibo_dict.get(n - 1)
    if not n1:
        n1 = fibo(n - 1)
    n2 = fibo_dict.get(n - 2)
    if not n2:
        n2 = fibo(n - 2)
    fibo_n = n1 + n2
    fibo_dict[n] = fibo_n
    return fibo_n

def solution(n):
    answer = 0
    fibo_num = fibo(n)
    answer = fibo_num % 1234567
    return answer

solution(3)