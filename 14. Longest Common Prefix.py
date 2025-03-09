
strs = ["flower","flow","flight"]

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strr = ""

        for i in range(len(strs[0])):
            for j in strs:  # Iterate strs every items
                if i == len(j) or strs[0][i] != j[i]:
                    return strr
            strr += strs[0][i]

        return strr

ss = Solution()
print(ss.longestCommonPrefix(strs))