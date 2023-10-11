fs = open ('students.txt','r',encoding='utf-8')

students = []
for student in fs :
    s = student.split(';')
    id = int(s[0])
    var = int (s[2])
    grup =(s[3])
    name = s[1] 
    students.append({'id': id, 'full_name': name,'var' : var, 'grup' : grup})   
for student in students:
    print(student)
fs.close()

'''

student1 =  {'id': 1, 'full_name': 'Алекберов Рамиль Русланович'}
student2 = {'id': 2, 'full_name': 'Бобровская Анастасия Дмитриевна','var':1}
student3 = {'id': 3, 'full_name': 'Винговатов Александр Олегович','var':2}

students =[]
students.append(student1)
students.append(student2)
students.append(student3)

for student in students:
    if 'var' in student:
        print (f"{student ['full_name']}  -  {student['var']}")

'''