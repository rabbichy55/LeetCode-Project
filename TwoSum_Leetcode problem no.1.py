nums = [2, 7, 11, 15]
target = 9

def twosum(nums, target):
    hash_map = {}

    for i, num in enumerate(nums):
        value = target - num

        if value in hash_map:
            return [hash_map[value], i]   # return indexes of nums
        hash_map[num] = i

    return []

print(twosum(nums, target))
# test case develop
# test case develop
# test case develop
# test case develop
# test case develop