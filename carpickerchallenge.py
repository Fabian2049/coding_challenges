import random
cars = input("pls enter your preferred car with (,_)   ")
car_list = cars.split(",")
print(car_list)
randomcar = random.choice(car_list)
print(randomcar)

# Project Idea: Randomized Quiz Generator
# Project Description:
# Create a quiz generator program that generates random quizzes from a set of questions and answers. The program should randomly select questions from different categories and present them to the user. After answering the quiz, the user receives a score and feedback.

# Key Features:

# Question Bank Creation: Define a question bank using Python lists and dictionaries. Each question can have multiple-choice answers with one correct answer.
# Randomized Quiz Generation: Randomly select a fixed number of questions (e.g., 10 questions) from the question bank to create a quiz.
# User Interaction: Display each question with its multiple-choice options to the user. Prompt the user to select an answer.
# Scoring System: Calculate and display the user's score based on the number of correct answers.
# Feedback: Provide feedback to the user based on their performance (e.g., "Great job!", "You can do better next time!").
