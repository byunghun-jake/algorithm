# 두 사람이 찾아야 하는 페이지를 찾을 때 까지 탐색을 몇 번 이어나가는지 세기

def binary_search(start, end, page, count):
    l = start
    r = end
    mid = (l + r) // 2
    count += 1

    # 만약 찾았다면?
    if mid == page:
        return count

    # 못찾았다면?
    elif page < mid:
        return binary_search(l, mid, page, count)
    else:
        return binary_search(mid, r, page, count)

T = int(input())

for tc in range(1, T + 1):
    P, PA, PB = map(int, input().split())

    # 이진 탐색 시작
    countA = binary_search(1, P, PA, 0)
    countB = binary_search(1, P, PB, 0)

    if countA < countB:
        print(f"#{tc} A")
    elif countA > countB:
        print(f"#{tc} B")
    else:
        print(f"#{tc} 0")
