if __name__ == '__main__':   
    student=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name,score])
    
    # Get the unique grades of students
    grades = []
    for _, score in student:
        if score not in grades:  # Ensuring uniqueness manually
            grades.append(score)
    grades.sort()
    second_lowest= grades[1]
    
    second_lowest_student=[name for name,score in student if score==second_lowest]
    
for name in sorted(second_lowest_student):
        print(name)
