word = list(input())

for idx in range(len(word)):
    word[idx] = word[idx].upper()

set_word = list(set(word))
counting_list = [0] * len(set_word)

max_count = 0
max_idx = 0
for letter in word:
    for i in range(len(set_word)):
        if letter == set_word[i]:
            counting_list[i] += 1
            if max_count < counting_list[i]:
                max_count = counting_list[i]
                max_idx = i


for i in range(len(counting_list)):
    if max_count == counting_list[i]:
        if max_idx != i:
            print("?")
            break
else:
    print(set_word[max_idx])

