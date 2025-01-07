def register_student(student: dict[str, dict[str, str]]) -> None:

    #student nomli dictionary ga "name" nomli key va unga foydalanuvchi kiritgan name ni kiritdik
    student['name'] = input("Enter your name: ")

    # student nomli dictionaryga 'courses' nomli list ham qo`shib qo`yaman, bu erda ta`labalarning yozilgan kurslari saqlanadi
    student['course'] = []

    # gmail va password ni alohida o`zgaruvchilarga olib oldik
    student_email = input("Enter your email: ")
    student_password = input("Enter your password: ")
    
    # student nomli dictionary ga pas_log nomli nestted dictionary yaratib oldik passwod va loginni saqlash uchun
    student['pas_log'] = {}
    student['pas_log']['log'] = student_email#pas_log nomli dictionary ga "log" nomli key va unga foydalanuvchi kiritgan loginni ni kiritdik
    student['pas_log']['pass'] = student_password#pas_log nomli dictionary ga "pass" nomli key va unga foydalanuvchi kiritgan parolni ni kiritdik
   
    return student

# paroli va logini bo`yicha bazada borligini aniqlovchi function
def login_student(students_data: list) -> str | None:
   
    # gmail va password ni kiriting 
    login = input("Enter your email: ")
    passwod = input("Enter your password: ")

    student_dict = {}
    student_dict['log'] = login
    student_dict['pass'] = passwod
    
    # bazada kiritilgan login va password ruyxatdan o`tgan yoki o`tmaganini tikshiramiz
    for user in students_data:
        if(user['pas_log']) == student_dict:
            print("Login successful! Welcome back, {}.".format(user['name']))
            return user
    return None

# kursga yozilish uchun function
def enroll_in_course(
    courses_data: list[dict[str, str]], 
    students_data: dict[str, dict[str, list[str]]], 
    student_email: str
) -> None:
    # kursni tanlash uchun nommir tanlash
    courses_number = int(input("Select a course number to enroll: "))

    if courses_number - 1 > len(courses_data) or courses_number - 1 < 0:
        print("\nSiz tanlagan nommirda kurs yo`q iltimos tikshirib qaytadan tanlang!\n")
        return None
    else:
        print("Successfully enrolled in {}!\n".format(courses_data[courses_number - 1]["course_name"]))
        return courses_data[courses_number - 1]
   