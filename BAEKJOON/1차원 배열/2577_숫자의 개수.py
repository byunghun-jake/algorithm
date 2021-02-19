digit_arr = [0] * 10
number = 1
for _ in range(3):
    input_num = int(input())
    number *= input_num

while number:
    remain = number % 10
    quotient = number // 10

    digit_arr[remain] += 1
    number = quotient

for i in range(len(digit_arr)):
    print(digit_arr[i])