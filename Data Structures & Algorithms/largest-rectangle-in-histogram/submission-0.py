class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #brute force solution is to compare all rectangles
        maxArea=heights[0]
        for i in range(len(heights)):
            height=heights[i]
            for j in range(i,len(heights)):
                height=min(height,heights[j])
                maxArea=max(maxArea,height*(j-i+1))
        return maxArea