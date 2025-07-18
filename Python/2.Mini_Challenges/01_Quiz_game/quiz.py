print("Welcome to the Computer Basic Concepts Quiz Game!")
play =str(input("Do you want play?(yes/no) "))
if play.lower() != "yes":
    quit()
else:
    print("Let's start the game!")

score = 0   # score counter
#QUESTION 1
answer = str(input("What does ROM stand for? ")).lower()
if answer == "read only memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
#QUESTION 2
answer = str(input("What does GPU stand for? ")).lower()
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
#QUESTION 3
answer = str(input("How many bits make a byte? "))
if answer == "8":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
#QUESTION 4
answer = str(input("What does GUI stand for? ")).lower()
if answer == "graphical user interface":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
#QUESTION 5
answer = str(input("What does CLI stand for? ")).lower()
if answer == "command line":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print(f"You got {(score/5) * 100} %")
print("You got " + str(score) + "questions correct!")

if score >= 3:
    print("Excellent, Job Well Done!")
else:
    print("Thanks For attempting the quiz!")
    print("Try Again to get a better score")