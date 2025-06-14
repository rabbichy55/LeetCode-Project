# binary search o(log n)
class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums)-1  # right = len(nums)-1 because list index count from 0

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left
nums = [1, 3, 5, 6]
target = 4

solution = Solution()
result = solution.searchInsert(nums, target)
print(result)
