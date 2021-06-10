# 8진수를 2진수로 바로 변경한다.
# 8진수의 수 하나를 3자리의 2진수로 변경하여 이어붙인다.

OCTAL_LIST = list(input())
result = ""

for i in range(len(OCTAL_LIST)):
    num = int(OCTAL_LIST[i])
    binary = ""
    while num:
        binary = str((num % 2)) + binary
        num //= 2
    if i != 0:
        while len(binary) != 3:
            binary = "0" + binary
    result += binary

if result:
    print(result)
else:
    print(0)



# -------------------------------------------------------------------------
# 8진수를 10진수로 변경한다.
# 10진수를 2진수로 변경한다.

# def octal_to_decimal(octal):
#     result = 0
#     i = 0
#     while octal:
#         num = octal % 10
#         result += num * (8 ** i)
#         octal //= 10
#         i += 1
#     return result
#
# def decimal_to_binary(decimal):
#     result = ""
#     while decimal:
#         result = str(decimal % 2) + result
#         decimal //= 2
#     return result
#
# decimal_num = octal_to_decimal(int(input()))
# print(decimal_to_binary(decimal_num))