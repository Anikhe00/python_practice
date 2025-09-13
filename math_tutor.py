print('Project - Math Tutor')

import random

# User specifies number of random practice questions
no_questions = int(input("Enter number of practice questions: "))

# user is presented with a prompt e.g 5 X 5 = and inputs the answer for each of the question
operators = ['+', '-', '*', '/' ]

correct_answers = 0
total_answers = 0

question_list = []

for i in range(no_questions):
    num1 = random.randint(1, 9)
    operator = random.choice(operators)
    num2 = random.randint(1, 9)
    
    expression = f"{num1} {operator} {num2}"
    answer = eval(expression)
    
    question = input(f"Question {i + 1}: {expression} = ")
    total_answers += 1
    
    summary = (expression, question, answer)
    question_list.append(summary)

    if question == str(answer):
        correct_answers += 1
    

print("=== Result ===")

for quiz in question_list:
    expression, question, answer = quiz
    print(f"Question: {expression} = {question}, Correct Answer: {answer}")

print(f"Your score is {correct_answers} out of {total_answers}")
print(f"Percentage of correct answers: {round((correct_answers / total_answers) * 100, 2)}%")
    