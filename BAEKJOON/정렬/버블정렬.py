# 2중 반복문을 이용해 값을 비교하며 그때그때 값을 교환하는 방식
# 시간 복잡도: O(n^2)

def bubbleSort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                continue
            elif nums[i] >= nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

def main():
    NUMS = [5, 3, 1, 4, 2]
    sorted_nums = bubbleSort(NUMS)
    print(sorted_nums)

main()