# 문자열을 순환하며, 문자를 배열에 추가한다.
# 문자를 추가하기 전, 배열에 문자가 있는지 확인한다.
# 만약 배열에 문자가 있는데, 마지막 순서에 있는 것이 아니라면 그 문자열은 그룹 단어가 아니다.
T = int(input())

count = 0
for tc in range(T):
    letter_list = []
    WORD = input()
    for letter in WORD:
        if letter not in letter_list:
            letter_list.append(letter)
        elif letter != letter_list[-1]:
            break
    else:
        count += 1

print(count)
