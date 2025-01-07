from school import students, courses, grades

def main():
    """
    Main function that drives the On-School system. It displays the main menu, 
    handles user registration and login, and provides an interface for enrolled students 
    to interact with courses and check grades.
    """
    # talabalarni ma`lumotlarini olish un bo`sh dictionary yaratib oldim
    student = {}

    # Talabalarni saqlash un ustoz bizga tayyor qilib list yaratibdilar👍
    students_data = []

    courses_data = [
        {"course_name": "Python Basics", "instructor": "John Doe", "duration": "8 weeks", "price": 500},
        {"course_name": "Data Science 101", "instructor": "Jane Smith", "duration": "10 weeks", "price": 780}
    ]
    grades_data = {}
    while True:
        print("=== Welcome to On-School ===","1. Register","2. Login","3. Exit", sep="\n")
        choose_commond = int(input("Select an option: "))
        
        # agar foydalanuvchi 1 ni tanlasa ro`yxatdan o`tishga o`tadi
        if choose_commond == 1:
            
            students.register_student(student)
            
            
            #students_data (ya`ni talabalarni saqlash uchun list) ga talabani kiritamiz 
            students_data.append(student)
            print(students_data[0]["name"])
            break
        elif choose_commond == 2:
            students.login_student()
        elif choose_commond == 3:
            print("Darslarni qoldirishni hayolinga ham keltirma!!! ", "Ishlaringa omad!!", sep="\n")
            break
        else: print("Siz noto`gri buyrug` tanladingiz iltimos tikshirib qaytadan tiring: ", end="\n\n")

main()
'''
=== Welcome to On-School ===
1. Register
2. Login
3. Exit
Select an option: 1
Enter your name: Alice Smith
Enter your email: alice@example.com
Enter your password: password123
Registration successful! Welcome, Alice Smith.

'''
