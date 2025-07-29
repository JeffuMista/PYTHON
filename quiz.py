marks = 0
question_one = int(input("Which of the following is not a reason to study python (1. It is easy to learn, 2. In it interactive, 3. It is a versatile language, 4. It is exclusive to back-end systems): "))

question_two = int(input("Which of the following is not part of the mathematical expressions in python (1. - , 2. ** , 3. ^ , 4. %): "))
question_three = int(input("Python is best used to do all the following but one (1. Build front-end interfaces, 2. Build scalable websites, 3. Data science and Machine Learning, 4. Game development): "))  

if question_one == 4:
    marks += 10
elif question_one == 1 or question_one == 2 or question_one == 3:
    marks += 0
if question_two == 3:
    marks += 10
elif question_two == 1 or question_two == 2 or question_two == 4:
    marks += 0
if question_three == 1:
    marks += 10
elif question_three == 2 or question_three == 3 or question_three == 4:
    marks += 0
print(f"You scored {marks} marks out of 30.")