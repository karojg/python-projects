# new_dict = {new_key: new_value for (key, value) in dict.items() if test}
# new_dict = {new_key: new_value for new_key in list}

import random
import pandas

students = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student: random.randint(1, 100) for student in students}
print(students_score)

passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_dict = {word: len(word) for word in sentence.split()}
print(sentence_dict)


students_dict = {
    "student": ["Harry", "James", "Lily"],
    "score": [56, 76, 87]
}
student_data_frame = pandas.DataFrame(students_dict)
print(student_data_frame)
for (index, row) in student_data_frame.iterrows():
    if row.student == "Harry":
        print(row.score)