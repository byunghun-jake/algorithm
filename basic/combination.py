nums = [1, 2, 3, 4]
length = 2
combs = []

def get_combination(temp, s):
    if len(temp) == length:
        combs.append(temp)
        return
    for idx in range(s, len(nums)):
        # temp에 추가하고 다음으로 넘어가는 경우
        get_combination(temp + [nums[idx]], idx + 1)

get_combination([], 0)