a_code = ord("a")
z_code = ord("z")
L = z_code - a_code + 1
alphabet_counting_list = [-1] * L

word = input()
for idx in range(len(word)):
    alphabet_index = ord(word[idx]) - a_code
    if alphabet_counting_list[alphabet_index] == -1:
        alphabet_counting_list[alphabet_index] = idx

print(*alphabet_counting_list)
