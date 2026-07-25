class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        #union find setup
        class UnionFind:
            def __init__(self,k):
                self.rank=[1]*k
                self.parents=[i for i in range(k)]
            def find(self, n):
                if self.parents[n]!=n:
                    self.parents[n]=self.find(self.parents[n])
                return self.parents[n]
            def union(self,n1,n2):
                p1,p2=self.find(n1), self.find(n2)
                if p1==p2:
                    return False
                if self.rank[p2]> self.rank[p1]:
                    self.parents[p1]=p2
                elif self.rank[p1]> self.rank[p2]:
                    self.parents[p2]=p1
                else:  
                    self.parents[p2]=p1
                    self.rank[p1]+=1
                return True

        def prime_factors(n):
            factors = set()
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factors.add(d)
                    n //= d
                d += 1
            if n > 1:
                factors.add(n)
            return factors
        prime_to_index = {}  # prime → first index with this prime

        unionFind=UnionFind(len(nums))
        for i, num in enumerate(nums):
            for prime in prime_factors(num):
                if prime in prime_to_index:
                    unionFind.union(i, prime_to_index[prime])
                else:
                    prime_to_index[prime] = i
        roots = set(unionFind.find(i) for i in range(len(nums)))
        return len(roots) == 1