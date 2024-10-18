# Initial score and list of students
all_students = []
final_scores = []

# Questions and answers
questions = [
    "What is the most widely spoken language in the world?\n a.)Chinese \n b.)Spanish \n c.)Arabic \n d.)English \n  ",
    "Where is the capital of Austria?\n a.)Tel Aviv \n b.)Madrid \n c.)Vienna \n d.)Frankfurt \n  ",
    "Who is the current President of Nigeria?\n a.)Goodluck Jonathan \n b.)Muhammadu Buhari \n c.)Bola Ahmed Tinubu \n d.)T-Pain \n  ",
    "Who was the first man in space?\n a.)Niel Armstrong \n b.)Yuri Gagarin \n c.)Vladimir Makarov \n d.)Vladimir Putin \n  ",
    "Which company is currently the richest in the world?\n a.)Microsoft \n b.)SpaceX \n c.)Apple \n d.)IBM \n  ",
]

answers = ['d', 'c', 'c', 'b', 'c']

# Retrieve the number of students
num_students = int(input("How many students would be taking this test?: "))

# retrieve students' names
for i in range(num_students):
    student_name = input(f"Student {i+1} - What is your name: ")
    all_students.append(student_name)

#test taking
for student in all_students:
    score = 0 
    print(f"\n{student}, it's your turn to take the test!")
    
    
    for question, answer in zip(questions, answers):
        print(question)
        user_answer = input("Answer: ")
        if user_answer.lower() == answer:  
            score += 1  
    
    # Append the student's final scores
    final_scores.append(score)

# Print each student's score
for i in range(num_students):
    print(f"{all_students[i]}'s score is {final_scores[i]}/5")

# Implementing the mean score
mean_score = sum(final_scores) / len(final_scores)
print(f"\nThe Average (mean) Score is {mean_score}")

# Minimum score
low_score_index = final_scores.index(min(final_scores))
print(f"\nThe Student with the Lowest Score is {all_students[low_score_index].capitalize()}")

# Maximum score
high_score_index = final_scores.index(max(final_scores))
print(f"\nThe Student with the Highest Score is {all_students[high_score_index].capitalize()}")
