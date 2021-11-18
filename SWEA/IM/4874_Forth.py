T = int(input())

for _ in range(T):
    data = input().split()
    stack = []

    for w in data:
        if w == "+":
            if len(stack) < 2:
                print("error")
                break
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n1 + n2)
        elif w == "*":
            if len(stack) < 2:
                print("error")
                break
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append((n1 * n2))
        elif w == "-":
            if len(stack) < 2:
                print("error")
                break
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append((n1 - n2))
        elif w == "/":
            if len(stack) < 2:
                print("error")
                break
            else:
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append((n1 // n2))
        elif w == ".":
            if len(stack) == 1:
                print(stack[0])
            else:
                print("error")
                break
        else:
            stack.append(int(w))