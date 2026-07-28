class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            x *= -1
            flag = -1

        ans = 0
        while x > 0:
            d = x % 10
            ans = ans * 10 + d
            x = x // 10
        ans *= flag
        if ans < -pow(2,31) or ans > pow(2,31)-1:
            return 0
        return ans