A, B = map(int, input().split())

reversed_A = 0
reversed_B = 0
for i in range(2, -1, -1):
    reversed_A += (A % 10) * (10 ** i)
    reversed_B += (B % 10) * (10 ** i)
    A //= 10
    B //= 10

if reversed_A > reversed_B:
    print(reversed_A)
else:
    print(reversed_B)
