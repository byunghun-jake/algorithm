# N = 100,000

# 몇 번째 수까지 담았는지 check

N = int(input())

nums = []
max_num = 0
answer = []

for _ in range(N):
  num = int(input())
  if max_num < num:
    for i in range(max_num + 1, num + 1):
      answer.append("+")
      nums.append(i)
    answer.append("-")
    nums.pop()
    max_num = num
  elif max_num > num:
    if nums[-1] == num:
      nums.pop()
      answer.append("-")
      max_num = max(max_num, num)
    else:
      print("NO")
      break
else:
  for a in answer:
    print(a)
