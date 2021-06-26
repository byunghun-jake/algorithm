# 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램 작성

import sys

class Stack:
    def __init__(self):
        self.x = 0
        self.size = 0
        self.arr = []

    def push(self, x):
        self.arr.append(x)
        self.size += 1

    def pop(self):
        if self.empty():
            return -1
        else:
            self.size -= 1
            return self.arr.pop()

    def empty(self):
        if self.size == 0:
            return 1
        else:
            return 0


    def top(self):
        if self.empty():
            return -1
        else:
            return self.arr[self.size - 1]

stack = Stack()
N = int(sys.stdin.readline().strip())
for _ in range(N):
    command = sys.stdin.readline().strip().split()
    if command[0] == "push":
        num = int(command[1])
        stack.push(num)
    if command[0] == "pop":
        print(stack.pop())
    if command[0] == "empty":
        print(stack.empty())
    if command[0] == "top":
        print(stack.top())
    if command[0] == "size":
        print(stack.size)


