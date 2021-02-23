# N: 분해합
# result: 생성자
N = int(input())
result = 0
start_num = N // 2
for i in range(start_num, N):
    num = i
    total = num
    while num:
        total += num % 10
        num //= 10
    if total == N:
        result = i
        break

print(result)
























