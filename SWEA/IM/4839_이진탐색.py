T = int(input())

def binary_search(l, r, target, count):
    # mid = int((l + r) / 2)
    mid = (l + r) // 2
    if target == mid:
        return count

    if target < mid:
        return binary_search(l, mid, target, count + 1)
    if mid < target:
        return binary_search(mid, r, target, count + 1)


for _ in range(T):
    P, A, B = map(int, input().split())

    count_a = binary_search(1, P, A, 1)
    count_b = binary_search(1, P, B, 1)

    if count_a == count_b:
        print(0)
    elif count_a < count_b:
        print("A")
    elif count_a > count_b:
        print("B")