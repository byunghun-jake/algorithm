# A를 B번 곱한 수를 구할 때, 분할정복을 이용해보자
# A^B
# B가 짝수일 때
    # A^B = A^(B//2) * A^(B//2 + 1)

A, B, C = map(int, input().split())

answer = 1

cache = []
# for i in range(100):
#     cache[i] =

# 이 부분을 어떻게 개선할까?
# for _ in range(B):
#     answer *= A

def divide_conquer(b):
    if b > 100:
        res = divide_conquer(b // 2)
        if b % 2 == 0:
            res = res * res
        else:
            res = res * res * A
    # else:
    #     for _ in range(b):

answer %= C
print(answer)