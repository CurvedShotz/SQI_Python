#A Simple CBT App
#Initial score and list of students
score = 0
all_students = []
final_scores = []

#Questions
questions = [
    "What is the most widely spoken language in the world?\n a.)Chinese \n b.)Spanish \n c.)Arabic \n d.)English \n  ",
    "Where is the capital of Austria?\n a.)Tel Aviv \n b.)Madrid \n c.)Vienna \n d.)Frankfurt \n Answer: ",
    "Who is the current President of Nigeria?\n a.)Goodluck Jonathan \n b.)Muhammadu Buhari \n c.)Bola Ahmed Tinubu \n d.)T-Pain \n  ",
    "Who was the first man in space?\n a.)Niel Armstrong \n b.)Yuri Gagarin \n c.)Vladimir Makarov \n d.)Vladimir Putin \n  ",
    "Which company is currently the richest in the world?\n a.)Microsoft \n b.)SpaceX \n c.)Apple \n d.)IBM \n  ",
]

answers = ['d','c','c','b','c']

#Retrieve Number of Students
num_students = int(input("How many students would be taking this test?: "))

#Retrieve said students' names
for i in range(num_students):
    students = input(f"Student{i+1} - What is your name: ")
    all_students.append(students)

# for questions, answers in zip(questions, answers):
#     print(questions)
#     answer = input('Answer: ')
#     if answer.lower() == answers:
#         print('Correct')
#         score += 1
#     else:
#         print('wrong')
#     final_scores.append(score)
for question, answer in zip(questions,answers):
    print(question)
    userAnswer = input("Answer: ")
    if userAnswer == answer:
        score += 1
    else:
        pass
    final_scores.append(score)


    
for i in range(num_students):
    print(f'{all_students[i]}\'s score is {final_scores[i]}/5')

#Implementing A Mean Score
meanScore = sum(final_scores)/len(final_scores)
print(f'\n The Average(mean) Score is {meanScore}')

#Minimum Score
lowScoreIndex = final_scores.index(min(final_scores))
print(f'\n The Student With The Lowest Score is {(all_students[lowScoreIndex].capitalize())}')

#Maximum Score
highScoreIndex = final_scores.index(max(final_scores))
print(f'\n The Student With The Highest Score is {(all_students[highScoreIndex].capitalize())}')


