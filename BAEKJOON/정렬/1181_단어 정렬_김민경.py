import sys

# sys.stdin = open("input.txt")

T = int(sys.stdin.readline())

arr = []
for _ in range(T):
    word = sys.stdin.readline().strip()
    arr.append(word)

def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while len(left) > left_idx and len(right) > right_idx:
        if left[left_idx] == right[right_idx]:
            if left[left_idx] < right[right_idx]:
                result.append(left[left_idx])
                left_idx += 1
            else:
                result.append(right[right_idx])
                right_idx += 1
        elif left[left_idx] < right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    if len(left) > left_idx:
        result += left[left_idx:]
    elif len(right) > right_idx:
        result += right[right_idx:]

    return result


def merge_Sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_Sort(a[:mid])
    right = merge_Sort(a[mid:])
    return merge(left, right)


n_arr = list(set(arr))
print(n_arr)
# result = SortList(n_arr)
final = merge_Sort(n_arr)

for i in range(len(final)):
    print(final[i])