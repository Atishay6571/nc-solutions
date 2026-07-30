class Solution:
    def candy(self, ratings: List[int]) -> int:
        #The greedy insight: separate the two constraints into independent passes. 
        #Each pass is simple and doesn't affect the other because of max.
        # LEFT to RIGHT PASS: only checks for right being greater

        candies=[ 1 for i in range(len(ratings))]
        # left to right pass
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candies[i]= candies[i-1]+1
        #right to left pass
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candies[i]=max(candies[i+1]+1, candies[i])
        return sum(candies)
