if __name__ == '__main__':
    n = int(input()) # number of students
    student_marks = {} # dictionary for student name and marks
    for _ in range(n):
        name, *line = input().split() # input name and marks separated by space
        scores = list(map(float, line)) # marks or scores into list as float
        student_marks[name] = scores
    query_name = input()
    
# marks that are 3 only in the list
# output : avg of marks for student name mentioned and round to 2 decimal places
marks = student_marks[query_name]
avg = sum(marks)/3
print(f'{avg:.2f}')
