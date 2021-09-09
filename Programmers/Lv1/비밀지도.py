def d_to_b(n, num):
    # n: number(10진수)
    binary_text = format(num, "b")
    l = n - len(binary_text)
    binary_text = "0" * l + binary_text
    return binary_text


def solution(n, arr1, arr2):
    answer = []
    # 숫자 배열을 이진수로 변환한다.
    bi_arr1 = []
    bi_arr2 = []
    for i in range(n):
        # 변환한 이진수를 배열에 저장한다.
        bi_arr1.append(d_to_b(n, arr1[i]))
        bi_arr2.append(d_to_b(n, arr2[i]))
    # 두 배열을 인덱스로 순회하며, 새로운 배열을 만든다.
    for i in range(n):
        temp_row = ""
        for j in range(n):
            # 벽은 "#"으로, 공백(0)은 " "으로 저장한다.
            temp = " "
            # 새로운 배열을 만들 때, 어느 하나라도 벽(1)인 부분이 있다면 벽이다.
            if bi_arr1[i][j] == "1" or bi_arr2[i][j] == "1":
                temp = "#"
            temp_row += temp
        # row 단위로 만들어진 문자열을 저장한다.
        answer.append(temp_row)
    print(arr1, arr2)
    return answer


print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))