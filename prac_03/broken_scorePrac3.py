def main():
    score_response = score()
    print(score_response)

def score():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
    elif score > 50 and score < 90:
        print("Passable")
    elif score > 90 and score < 100:
        print("Excellent")
    elif score < 50:
        print("Bad")

main()