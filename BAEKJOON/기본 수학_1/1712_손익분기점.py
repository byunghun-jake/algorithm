# A: 고정 비용
# B: 가변 비용(대당)
# C: 노트북 가격
# 손익 분기점
# A + B * x <= C * x
# A / (C - B) <= x
A, B, C = map(int, input().split())

if C <= B:
    print(-1)
else:
    x = A // (C - B)
    print(x + 1)





