if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        # students is the nested list
        

scores = []
for student in students:
    scores.append(student[1])

scores = sorted(set(scores))
# scores sorted in ascending order as a set
 
second_grade = scores[1]
# it is the second grade number

names = [] 
# second_grade_names = []

for item in students:
    if second_grade == item[1]:
        names.append(item[0])
        
names = sorted(names)

for i in names:
    print(i)

