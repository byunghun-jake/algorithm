# 검색 결과가 주어졌을 때, 어떤 패턴을 입력해야 그 결과가 나오는지 출력하는 문제이다.
# 패턴에는 알파벳, ".", "?"만 넣을 수 있으며, 가능하면 ?을 적게 써야 한다.
# 파일 이름의 길이는 모두 같다.

# N <= 50
# 모든 문자를 순회하며, 겹치는 부분이 있는지 확인한다.
# 겹치지 않는다.
    # 출력 값에 "?"를 삽입한다.
# 겹친다.
    # 해당 알파벳을 삽입한다.

N = int(input())
L = 0
NAMES = []

for _ in range(N):
    S = input()
    L = len(S)
    NAMES.append(S)

result = ""
for i in range(L):
    is_match = True
    letter = ""
    for name in NAMES:
        if not letter:
            letter = name[i]
        elif letter != name[i]:
            is_match = False
            break
    if is_match:
        result += letter
    else:
        result += "?"
print(result)