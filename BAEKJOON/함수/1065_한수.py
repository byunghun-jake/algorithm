def hansu(n):
    if n < 100:
        return True

    digit_list = []
    gap = 0
    i = -1
    while n:
        remain = n % 10
        digit_list.append(remain)
        i += 1
        n //= 10
        if i == 0:
            continue
        elif i == 1:
            gap = digit_list[i] - digit_list[i-1]
        else:
            if digit_list[i] - digit_list[i-1] != gap:
                return False
    else:
        return True


N = int(input())
count = 0
for num in range(1, N+1):
    if hansu(num):
        count += 1

print(count)

















