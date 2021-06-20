# 2중 반복문을 순회하며, 최소값(혹은 최대값)을 갖는 인덱스를 찾아 2차 반복문을 수행한 뒤 기준 값을 교환합니다.
# 시간 복잡도: O(n^2)

def selectionSort(nums):
    for i in range(len(nums)):
        min_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        else:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


def main():
    NUMS = [3, 1, 4, 2]
    result = selectionSort(NUMS)
    print(result)

main()
