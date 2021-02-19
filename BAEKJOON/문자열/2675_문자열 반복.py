T = int(input())
for tc in range(T):
    R, S = input().split()
    R = int(R)

    ans = ""
    for letter in S:
        ans += letter*R

    print(ans)




