def find_duplicate(nums):
    if not nums or isinstance(nums, str):
        return False

    nums_set = set()
    for num in nums:
        if isinstance(num, str) or num < 1:
            return False
        if num in nums_set:
            return num
        nums_set.add(num)

    return False

    raise NotImplementedError
