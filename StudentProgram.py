import StudentClass as S

def main():
    student_id = 1001
    name = 'John'
    dob = '16/06/2002'
    classification = 'Jr'

    student1 = S.Student(student_id, name, dob, classification)
    
    student1.age()
    student1.calc_register()

    print(f'Student age is: {student1.get_age()}')
    print(f'{student1.get_register()}')

main()