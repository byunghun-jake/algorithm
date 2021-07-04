import sys

class Deque:
    def __init__(self):
        self.deque = []

    def size(self):
        return len(self.deque)

    def empty(self):
        return 1 if self.size() == 0 else 0

    def front(self):
        return -1 if self.empty() else self.deque[0]

    def back(self):
        return -1 if self.empty() else self.deque[-1]

    def push_front(self, x):
        self.deque = [x] + self.deque

    def push_back(self, x):
        self.deque.append(x)

    def pop_front(self):
        return -1 if self.empty() else self.deque.pop(0)

    def pop_back(self):
        return -1 if self.empty() else self.deque.pop()


N = int(input())
de = Deque()

for _ in range(N):
    operation = sys.stdin.readline().strip().split()
    if operation[0] == "push_back":
        de.push_back(operation[1])
    elif operation[0] == "push_front":
        de.push_front(operation[1])
    elif operation[0] == "front":
        print(de.front())
    elif operation[0] == "back":
        print(de.back())
    elif operation[0] == "pop_front":
        print(de.pop_front())
    elif operation[0] == "pop_back":
        print(de.pop_back())
    elif operation[0] == "size":
        print(de.size())
    elif operation[0] == "empty":
        print(de.empty())
