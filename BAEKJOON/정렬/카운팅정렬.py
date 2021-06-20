# 정수만 정렬이 가능하다.
# 정수의 값을 곧 인덱스로 같는 counting 배열을 생성하여, 해당하는 값이 몇 개가 있는지 확인한다.

def countingSort(nums):
    counting_arr = [0] * (max(nums) + 1)
    temp = [-1] * len(nums)
    for i in range(len(nums)):
        counting_arr[nums[i]] += 1
    for i in range(1, len(counting_arr)):
        counting_arr[i] += counting_arr[i - 1]

    for i in range(len(nums)):
        counting_arr[nums[i]] -= 1
        temp[counting_arr[nums[i]]] = nums[i]
    return temp


def main():
    NUMS = [3, 4, 1, 4, 2, 0]
    result = countingSort(NUMS)
    print(result)


main()

# # [1, 1, 1, 1, 2]
# [1, 2, 3, 4, 6]
#
# [-1, -1, -1, -1, -1, -1]
#
# [-1, -1, -1, -1, 3, -1]
