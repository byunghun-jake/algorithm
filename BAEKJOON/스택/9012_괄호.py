# 여는 괄호가 없는데 닫는 괄호가 나오는 경우
# 모든 순환이 끝나고, stack에 남아있는 괄호가 있는 경우

N = int(input())

def check_bracket():
  stack = []
  for bracket in brackets:
    if bracket == "(":
      stack.append(bracket)
    else:
      if len(stack) == 0:
        print("NO")
        return
      else:
        stack.pop()
  if stack:
    print("NO")
    return
  print("YES")

for _ in range(N):
  brackets = input()
  check_bracket()