
N, K = map(int, input().split())

arr = [i for i in range(1, N + 1)]
result = []

idx = 0

while arr:
    idx = (idx + K - 1) % len(arr)
    result.append(f"{arr.pop(idx)}")

print(f"<{', '.join(result)}>")
