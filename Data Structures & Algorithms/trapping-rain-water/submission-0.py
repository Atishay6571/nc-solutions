class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        for i, ele in enumerate(height):
            l=i-1
            r=i+1
            lmax=rmax=ele
        
            while l>=0:
                lmax=max(lmax,height[l])
                l-=1
            while r<len(height):
                rmax=max(rmax,height[r])
                r+=1
            if min(lmax,rmax)>ele:
                water+=min(lmax,rmax)-ele
        return water