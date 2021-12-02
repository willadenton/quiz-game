# A silly little quiz

# import prompt and answer from Question.py
from Question import Question

# questions used in quiz and answer options
question_prompts = [
    "Who invented the word vomit?\n(a) William Shakespeare\n(b) Little Tommy\n(c) Herbert Hoover\n\n",
    "What's the hottest planet in the solar system'?\n(a) Uranus\n(b) Mars\n(c) Venus\n\n",
    "What is the only edible food that never goes bad?\n(a) Rice\n(b) Honey\n(c) Cornflakes\n\n",
    "Which country invented ice cream?\n(a) Thailand\n(b) China\n(c) France\n\n",
    "What shape is a stop sign?\n(a) Hexagon\n(b) Pentagon\n(c) Octagon\n\n "
]

# answer key 
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    Question(question_prompts[3], "b"),
    Question(question_prompts[4], "c")
]

# how to calculate and display score at the end
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct!")

run_test(questions)