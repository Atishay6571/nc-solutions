class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        reset=0
        while sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                reset =0
            else:
                stud = students.pop(0)
                students.append(stud)
                reset+=1
            if reset == len(students):
                break
        return len(students)
                

    