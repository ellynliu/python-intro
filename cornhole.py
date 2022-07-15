# Take in user input, calculate each team's score in cornhole
# using cancellation scoring. Game ends when one team reaches 21 points.
def cornhole():
    red_score = 0
    blue_score = 0
    round = 1

    while red_score < 21 and blue_score < 21:
        print(f"Round {round}")
        round += 1
        r = input("Enter red's points: ")
        while not r.isnumeric():
            r = input("Enter red's points: ")
        r = int(r)

        b = input("Enter blue's points: ")
        while not b.isnumeric():
            b = input("Enter blue's points: ")
        b = int(b)
        if r > b:
            red_score += (r - b)
        else:
            blue_score += (b - r)
        print(f"Red: {red_score} | Blue: {blue_score}")
    if red_score >= 21:
        print("Red won!")
    else:
        print("Blue won!")

cornhole()
