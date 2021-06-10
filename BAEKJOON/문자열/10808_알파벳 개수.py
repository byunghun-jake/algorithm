# 소문자로만 이루어진 단어 S가 주어진다.
# 각 알파벳이 몇 개가 들어있는지 구하는 프로그램을 작성하시오.

# 아스키 코드 ord() 이용
# 각 알파벳의 인덱스를 갖는, 개수를 담는 배열을 만든다.
# 주어진 단어를 하나씩 순회하며, 배열에 개수를 더해준다.
# 배열을 푼 후 출력한다.

ALPHABET_LIST = [0] * (ord("z") - ord("a") + 1)
# a ~ z까지 담을 수 있는 배열이 필요한 것이기에, 1을 더해주어야 한다.

S = input()

for letter in S:
    ALPHABET_LIST[ord(letter) - ord("a")] += 1

print(*ALPHABET_LIST)