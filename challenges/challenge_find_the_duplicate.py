def find_duplicate(nums):
    if not nums or isinstance(nums, str) or len(nums) < 2:
        return False

    nums_set = set()
    for num in nums:
        if not isinstance(num, int) or num < 1:
            return False
        if num in nums_set:
            return num
        nums_set.add(num)

    return False
