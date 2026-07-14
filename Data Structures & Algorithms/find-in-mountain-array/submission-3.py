class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length=mountainArr.length()
        l,r=0,length-1

        while l<=r:
            m=(l+r)//2
            left,mid,right= mountainArr.get(m-1),mountainArr.get(m),mountainArr.get(m+1)
            if left<mid<right:
                l=m+1
            elif left>mid>right:
                r=m-1
            else:
                break
        peak=m
        if target>mountainArr.get(peak):
            return -1
        #for Left sorted array
        l,r=0,peak-1
        while l<=r:
            m=(l+r)//2
            mid= mountainArr.get(m)
            if target>mid:
                l=m+1
            elif target<mid:
                r=m-1
            else:
                return m
        #for Right sorted array
        l,r=peak,length-1
        while l<=r:
            m=(l+r)//2
            mid= mountainArr.get(m)
            if target>mid:
                r=m-1
            elif target<mid:
                l=m+1
            else:
                return m
        return -1
        
            
