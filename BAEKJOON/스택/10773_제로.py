import sys

stack = []

N = int(sys.stdin.readline().strip())

for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)
print(sum(stack))