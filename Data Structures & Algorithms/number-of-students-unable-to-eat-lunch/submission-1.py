class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        zero = students.count(0)
        one = students.count(1)
        stack = 0
        for i in range(len(students)):
            if sandwiches[i]==0 and zero>0:
                zero-=1

            elif sandwiches[i]==1 and one>0:
                one-=1
            else:
                return len(students)-i
        return 0
            
    