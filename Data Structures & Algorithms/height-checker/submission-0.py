class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        count = 0
        for i in range(len(heights)):
            count+= 1 if expected[i]!=heights[i] else 0
        return count