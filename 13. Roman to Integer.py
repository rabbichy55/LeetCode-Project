a = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000
}
s = input()
class Solution:
    def romanToInt(self, s: str) -> int:

        v = {"IV": 4,
             "IX": 9,
             "XL": 40,
             "XC": 90,
             "CD": 400,
             "CM": 900
             }
        output = 0

        for i in range(len(s)):  # s length
            if s[i: i+2] in v:   # Check s in v set
                output += v[s[i:i+2]]  # v index add to output
                output -= a[s[i+1]]    # Subtract extra value
            else:
                output += a[s[i]]

        return output
ss = Solution()
print(ss.romanToInt(s))

