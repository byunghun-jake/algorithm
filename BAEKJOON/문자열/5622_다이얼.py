dial = ["", "", "", "ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

# 입력받기
WORD = input()

time = 0
for letter in WORD:
    for i in range(len(dial)):
        if letter in dial[i]:
            time += i

print(time)
