T = int(input())

for _ in range(T):
    S1 = input()
    S2 = input()
    if S2.find(S1) != -1:
        print(1)
    else:
        print(0)