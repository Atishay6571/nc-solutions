class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        noteCount={5:0, 10:0, 20:0}
        for bill in bills:                
            if bill==10:
                if noteCount[5]>0:
                    noteCount[5]-=1
                else:
                    return False
#the greedy choice is use $10 before three $5s when making change for $20.
            elif bill==20:
                if (noteCount[5]>0 and noteCount[10]>0):
                    noteCount[10]-=1
                    noteCount[5]-=1
                elif (noteCount[5]>=3):
                    noteCount[5]-=3
                else:
                    return False
            noteCount[bill]+=1
        return True
