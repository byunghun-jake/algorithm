# A를 B번 곱한 수를 구할 때, 분할정복을 이용해보자
# A^B
# B가 짝수일 때
    # A^B = A^(B//2) * A^(B//2 + 1)

A, B, C = map(int, input().split())

# answer = 1

cache = []
# for i in range(100):
#     cache[i] =

# 이 부분을 어떻게 개선할까?
# for _ in range(B):
#     answer *= A

def divide_conquer(b):
    if b == 0:
        return 1

    n = divide_conquer(b // 2)

    if b % 2 == 0:
        return (n * n) % C
    else:
        return (n * n * A) % C

answer = divide_conquer(B)
print(answer)

###########
# 숫자가 너무 커지면, 나머지 연산도 오래걸린다는 걸 알 수 있었다.