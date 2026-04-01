if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        scores=[]
    for student in students:
        scores.append(student[1])
    sc=list(set(scores))
    sc.sort()
    if len(sc)>1:
        second_lowest=sc[1]
    else:
        second_lowest=None
    name=[]
    for student in students:
        if student[1]==second_lowest:
            name.append(student[0])
    name.sort()
    for n in name:
        print(n)
            
