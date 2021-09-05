lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def solution(s, n):
    answer = ''
    for letter in s:
        if letter == " ":
            answer += letter
        elif letter in lower:
            temp = lower.find(letter)
            temp += n
            temp %= len(lower)
            answer += lower[temp]
        else:
            temp = upper.find(letter)
            temp += n
            temp %= len(upper)
            answer += upper[temp]

    return answer