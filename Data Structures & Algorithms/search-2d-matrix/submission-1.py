class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        new=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                new.append(matrix[i][j])
        l,r=0,len(new)-1
        while l<=r:
            mid= (l+r)//2
            if new[mid]==target:
                return True
            elif new[mid]<target:
                l=mid+1
            elif new[mid]>target:
                r=mid-1
        return False