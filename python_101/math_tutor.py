print('Project - Math Tutor')

import random
from time import time as timer

# User specifies number of random practice questions
no_questions = int(input("Enter number of practice questions: "))

# user is presented with a prompt e.g 5 X 5 = and inputs the answer for each of the question
operators = ['+', '-', '*', '/' ]

correct_answers = 0
total_answers = 0

question_list = []

start_time = timer()

for i in range(no_questions):
    num1 = random.randint(1, 9)
    operator = random.choice(operators)
    num2 = random.randint(1, 9)
    
    expression = f"{num1} {operator} {num2}"
    answer = round(eval(expression), 2)
    
    question = input(f"Question {i + 1}: {expression} = ")
    total_answers += 1
    
    summary = (expression, question, answer)
    question_list.append(summary)

    if question == str(answer):
        correct_answers += 1

    end_time = timer()

print("\n=== Result ===\n")

print(f"Thank you for playing!\nYou got {correct_answers} out of {total_answers}, which is {round((correct_answers / total_answers) * 100, 2)}% correct in {round(end_time-start_time,1)} seconds ({round((end_time-start_time)/no_questions,1)}seconds/question)")

print("\n=== Questions ===\n")

for quiz in question_list:
    expression, question, answer = quiz
    print(f"Question: {expression} = {question}, Correct Answer: {answer}")