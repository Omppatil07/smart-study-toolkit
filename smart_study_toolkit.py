import turtle
import random
import time
print("SMART STUDY TOOLKIT")

# ---------------- QUIZ GAME ----------------

def quiz_game():

    score = 0
    print("\nQUIZ GAME")

    name = input("Enter your name: ")

    questions = [
        ("Who developed Python?", "guido"),
        ("Keyword used to define a function?", "def"),
        ("Which loop runs fixed number of times?", "for"),
        ("Which keyword is used for exception handling?", "try")
    ]

    random.shuffle(questions)

    for q, ans in questions:

        print("\nYou have 10 seconds to answer")

        start = time.time()

        user = input(q + " : ")

        end = time.time()
        total_time = end - start

        if total_time > 10:
            print("Time exceeded! Moving to next question.")
            continue

        if user.lower() == ans:
            print("Correct Answer!")
            score += 1
        else:
            print("Wrong Answer! Correct answer is:", ans)

    print("\nYour Final Score:", score)

    # SAVE SCORE TO FILE
    file = open("scores.txt", "a")
    file.write(name + " : " + str(score) + "\n")
    file.close()

# ---------------- SAVE NOTES ----------------
def save_notes():
    try:
        note = input("Enter your study note: ")

        file = open("notes.txt", "a")
        file.write(note + "\n")
        file.close()

        print("Note saved successfully!")

    except:
        print("Error saving note")


# ---------------- VIEW NOTES ----------------
def view_notes():
    try:
        file = open("notes.txt", "r")

        print("\nYour Saved Notes:")
        print("------------------")

        for line in file:
            print(line)

        file.close()

    except:
        print("No notes found!")


# ---------------- TURTLE PATTERN ----------------
def draw_pattern():

    import turtle
    import random

    import turtle
    import random

    try:
        turtle.clearscreen()
    except turtle.Terminator:
        pass

    screen = turtle.Screen()
    t = turtle.Turtle()

    screen.bgcolor("black")
    t.speed(3)
    t.width(2)

    colors = ["red","blue","green","yellow","purple","orange","pink"]

    print("\nChoose Pattern")
    print("1. Spiral Pattern")
    print("2. Star Pattern")
    print("3. Flower Pattern")
    print("4. Polygon Pattern")

    choice = input("Enter your choice: ")

    if choice == "1":

        for i in range(100):
            t.color(random.choice(colors))
            t.forward(i * 2)
            t.right(59)

    elif choice == "2":

        for i in range(50):
            t.color(random.choice(colors))
            t.forward(150)
            t.right(144)

    elif choice == "3":

        for i in range(36):
            t.color(random.choice(colors))
            t.circle(100)
            t.right(10)

    elif choice == "4":

        sides = int(input("Enter number of sides: "))
        angle = 360 / sides

        for i in range(sides):
            t.color(random.choice(colors))
            t.forward(100)
            t.right(angle)

    else:
        print("Invalid choice")
    print("Click the turtle window to close the drawing")
    turtle.exitonclick()


# ---------------- VIEW SCORES ----------------
def view_scores():

    print("\nQUIZ LEADERBOARD")
    print("------------------")

    try:
        file = open("scores.txt", "r")
        data = file.read()
        print(data)
        file.close()

    except:
        print("No scores available yet.")

# ---------------- MAIN MENU ----------------
while True:

    print("\n===== SMART STUDY TOOLKIT =====")
    print("1. Quiz Game")
    print("2. Save Study Notes")
    print("3. View Notes")
    print("4. Draw Turtle Pattern")
    print("5. View Quiz Scores")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        quiz_game()

    elif choice == "2":
        save_notes()

    elif choice == "3":
        view_notes()

    elif choice == "4":
        draw_pattern()

    elif choice == "5":
        view_scores()

    elif choice == "6":
        print("Thank you for using Smart Study Toolkit!")
        break

    else:
        print("Invalid choice. Please try again.")