class Student:
    """Represents a student with ideal properties."""

    def __init__(self, name, age, grade, gpa, extracurriculars):
        """Initializes a Student object with the given properties.

        Args:
            name (str): The student's full name.
            age (int): The student's age.
            grade (int): The student's grade level.
            gpa (float): The student's grade point average.
            extracurriculars (list): A list of extracurricular activities the student participates in.
        """
        self.name = name
        self.age = age
        self.grade = grade
        self.gpa = gpa
        self.extracurriculars = extracurriculars

    def study(self, hours):
        """Simulates the student studying for a given number of hours.

        Args:
            hours (int): The number of hours to study.
        """
        print(f"{self.name} is studying for {hours} hours.")
        self.gpa += 0.1  # Increase GPA by 0.1 for each hour studied

    def participate_in_extracurriculars(self):
        """Simulates the student participating in extracurricular activities."""
        print(f"{self.name} is participating in extracurricular activities.")

    def __str__(self):
        """Returns a string representation of the Student object."""
        return f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}\nGPA: {self.gpa}\nExtracurriculars: {self.extracurriculars}"

# Create an instance of the Student class
student1 = Student("John Doe", 17, 12, 4.0, ["Math Club", "Debate Team"])

# Access and modify the student's properties
print(student1.name)
student1.age = 18
print(student1.age)

# Call the student's methods
student1.study(3)
student1.participate_in_extracurriculars()

# Print the student's information
print(student1)