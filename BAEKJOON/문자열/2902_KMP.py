# 긴 형태의 알고리즘 이름이 주어졌을 때, 이를 짧은 형태로 변환하는 프로그램을 작성하시오.

# "-"로 구분되어 있기 때문에, split()을 이용해 각 이름을 분리한다.
# 배열을 순회하며, 요소의 0번째 문자를 가져와 붙여준다.

S = input()
S_LIST = S.split("-")
result = ""
for name in S_LIST:
    result += name[0]

print(result)