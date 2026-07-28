class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # dp solution
        # key idea: iterate through array thinking you popped that last
        # subproblems become to solve left and right independently
        # if you think about popping first then left and right subarrays
        # end up sharing a boundary 
        nums =[1]+nums+[1]
        dp={}
        def dfs(l,r):
            if l>r:
                return 0
            if (l,r) in dp:
                return dp[(l,r)]
            product=0
            for i in range(l,r+1):
                coins=nums[l-1]*nums[r+1]*nums[i]
                product=max(product, coins+dfs(l,i-1)+dfs(i+1,r))
            dp[(l,r)]=product
            return product
        return dfs(1,len(nums)-2)