class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        i = x
        reverse = 0
        while True:
            if i == 0:
                break
            else:
                a = i % 10
                reverse = reverse * 10 + a
            i = i // 10
        if reverse == x:
            return True
        else:
            return False
ss = Solution()
print(ss.isPalindrome(121))