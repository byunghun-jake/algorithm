# 1. 소수의 정의 그대로 2부터 num - 1까지의 수로 나누어 떨어지는 지 확인 (시간초과)
# def solution(n):
#     answer = 0
#     for num in range(2, n + 1):
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             answer += 1
#     return answer

# 2. num // 2까지의 수로 나누어 떨어지는지 확인 (시간초과)
# def solution(n):
#     answer = 0
#     for num in range(2, n + 1):
#         for i in range(2, num // 2 + 1):
#             if num % i == 0:
#                 break
#         else:
#             answer += 1
#     return answer

# 3. 제곱근 수(num ** 0.5)까지의 수로 나누어 떨어지는지 확인
def solution(n):
    answer = 0
    for num in range(2, n + 1):
        x = int(num ** 0.5)
        for i in range(2, x + 1):
            if num % i == 0:
                break
        else:
            answer += 1
    return answer

# 4. 에라토스테네스의 체로 소수목록을 추출한 뒤, 소수로 나누어떨어지는지 확인