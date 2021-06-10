# 알파벳 소문자로만 이루어진 단어가 주어질 때, 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
# 팰린드롬: 거꾸로 읽어도 동일한 단어

# 입력받은 문자를 뒤에서부터 순환하여 새로운 문자를 만든다.
# 두 문자를 비교한다.

S = input()

# reversed_S = ""
# for letter in S:
#     reversed_S = letter + reversed_S
#
# if S == reversed_S:
#     print(1)
# else:
#     print(0)

L = len(S)
for i in range(L // 2):
    s = S[i]
    e = S[L - i - 1]
    if s != e:
        print(0)
        break
else:
    print(1)