def register_student(students_data: student[str, dict[str, str]]) -> None:
    """
    Registers a new student by collecting their name, email, and password, 
    and stores the information in the students_data dictionary.

    Args:
        students_data (dict): A dictionary where student emails are keys 
                               and their details (name and password) are stored as values.
    """
    student['name'] = input("Enter your name: ")#student nomli dictionary ga "name" nomli key va unga foydalanuvchi kiritgan name ni kiritdik

    # gmail va password ni alohida o`zgaruvchilarga olib oldik
    student_email = input("Enter your email: ")
    student_password = input("Enter your password: ")
    
    # student nomli dictionary ga pas_log nomli nestted dictionary yaratib oldik passwod va loginni saqlash uchun
    student['pas_log'] = {}
    student['pas_log']['log'] = student_email#pas_log nomli dictionary ga "log" nomli key va unga foydalanuvchi kiritgan loginni ni kiritdik
    student['pas_log']['pass'] = student_password#pas_log nomli dictionary ga "pass" nomli key va unga foydalanuvchi kiritgan parolni ni kiritdik
            

def login_student(students_data: dict[str, dict[str, str]]) -> str | None:
    """
    Allows a student to log in by entering their email and password. 
    If the login is successful, it returns the student's name.

    Args:
        students_data (dict): A dictionary where student emails are keys 
                               and their details (name and password) are stored as values.

    Returns:
        str: The student's name if login is successful, else None.
    """
    pass

def enroll_in_course(
    courses_data: list[dict[str, str]], 
    students_data: dict[str, dict[str, list[str]]], 
    student_email: str
) -> None:
    """
    Allows a student to enroll in a course by selecting from the available courses. 
    The selected course is added to the student's list of enrolled courses.

    Args:
        courses_data (list): A list of dictionaries containing available course details.
        students_data (dict): A dictionary where student emails are keys 
                               and their details (including enrolled courses) are stored as values.
        student_email (str): The email of the student who is enrolling.
    """
    pass
