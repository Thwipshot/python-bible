from random import choice

questions = ["Why do you like board games?: ",
             "Why is the sky blue?: ",
             "Why is there a face on the moon?: ",
             "What is programming?: ",
             "Why can birds fly?: "]

question = choice(questions)
answer = input(question).lower()

while answer != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh... okay")
