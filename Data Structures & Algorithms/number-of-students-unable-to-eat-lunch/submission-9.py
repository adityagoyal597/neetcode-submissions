class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentHungry=len(students) #initially total no. of students

        count={} # Hashmap

        for student in students:
            if student not in count:
                count[student]=0
                count[student]+=1
            else:
                count[student]+=1

        for sandwich in sandwiches:
            if sandwich in count and count[sandwich]>0:
                count[sandwich]-=1
                studentHungry-=1
            else:
                break
        
        return studentHungry
            
