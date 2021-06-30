# 문자열을 처음부터 순환하며, 여는 괄호를 만나면 스택에 넣는다.
# 닫는 괄호가 나오면 스택의 최상단에 종류가 같은 여는 괄호가 있는지 확인하고, 일치하면 스택에서 뺀다.

bracket_dict = {
    "]": "[",
    ")": "("
}


def check_bracket(text):
    stack = []

    for word in text:
        if word == "[" or word == "(":
            stack.append(word)
        elif word == "]" or word == ")":
            if len(stack) == 0 or bracket_dict.get(word) != stack[-1]:
                print("no")
                return
            else:
                stack.pop()
    else:
        if len(stack) != 0:
            print("no")
            return
        else:
            print("yes")


while True:
    text = input()

    if text == ".":
        break
    check_bracket(text)
