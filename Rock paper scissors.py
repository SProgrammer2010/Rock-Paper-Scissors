import random

print("Rock, Paper, Scissors Game Designed in Python[Use R for rock, P for paper, S for scissors]")
moves = ["Rock", "Paper", "Scissors"]

while True:
    In = input("Enter move: ")
    m = random.choice(moves)
    if In == "R" and m == "Paper":
        print(m, "/You Lose!")
    if In == "P" and m == "Scissors":
        print(m, "/You Lose!")
    if In == "S" and m == "Rock":
        print(m, "/You Lose!")
    if In == "R" and m == "Scissors":
        print(m, "/You Win!")
    if In == "P" and m == "Rock":
        print(m, "/You Win!")
    if In == "S" and m == "Paper":
        print(m, "/You Win!")
    if In == "R" and m == "Rock":
        print("Draw!")
    if In == "P" and m == "Paper":
        print("Draw!")
    if In == "S" and m == "Scissors":
        print("Draw!")