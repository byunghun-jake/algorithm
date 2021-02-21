# 입력받기
WORD = input()

# 입력받은 글자를 순환하며, 크로아티아 알파벳 개수를 센다.
idx = 0
count = 0
while idx < len(WORD):
    if WORD[idx] == "c" and idx+1 < len(WORD) and (WORD[idx+1] == "=" or WORD[idx+1] == "-"):
        idx += 1
    elif WORD[idx] == "d":
        if idx+2 < len(WORD) and WORD[idx+1] == "z" and WORD[idx+2] == "=":
            idx += 2
        elif idx+1 < len(WORD) and WORD[idx+1] == "-":
            idx += 1
    elif (WORD[idx] == "l" or WORD[idx] == "n") and idx+1 < len(WORD) and WORD[idx+1] == "j":
        idx += 1
    elif (WORD[idx] == "s" or WORD[idx] == "z") and idx+1 < len(WORD) and WORD[idx+1] == "=":
        idx += 1
    count += 1
    idx += 1

print(count)












