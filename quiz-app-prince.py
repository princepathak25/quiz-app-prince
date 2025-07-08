while True:
    score=0
    print("🎓 Welcome to the Ultimate Quiz by Prince Pathak!\n")
    name = input("What's your name, champ? ")
    print(f"\n👋 Welcome, {name}! Get ready for the quiz!\n")
    print("Instructions:")
    print("1. Answer the questions by typing the letter of the correct option (a, b, or c).")
    print("2. Each correct answer earns you 1 point.")
    print("3. Let's see how many points you can score!\n")
    print("Let's begin the quiz! Good luck! 🍀\n")
    # Question 1
    q1 = input("1. What does HTML stand for?\n(a) HyperText Markup Language\n(b) HighText Machine Language\n(c) HyperTool Multi Language\nYour answer: ")
    if q1.lower() == 'a':
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is (a) HyperText Markup Language.\n")
    # Question 2
    q2 = input("2. Which keyword is used to define a function in Python?\n(a) func\n(b) define\n(c) def\nYour answer: ")
    if q2.lower() == 'c':
        print("✅ Correct!\n")
        score += 1  
    else:
        print("❌ Incorrect. The correct answer is (c) def.\n")
    # Question 3
    q3= input("3. What is the output of: print(2 ** 3)?\n(a) 6\n(b) 8\n(c) 9\nYour answer: ")
    if q3.lower() == 'b':
        print("✅ Correct!\n")
        score += 1  
    else:
        print("❌ Incorrect. The correct answer is (b) 8.\n")
    # Question 4
    q4 = input("4. Which of the following is a Python data type?\n(a) list\n(b) array\n(c) vector\nYour answer: ")
    if q4.lower() == 'a':
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is (a) list.\n")
    # Question 5
    q5 = input("5. Which of the following is a valid variable name in Python?\n(a) 1st_variable\n(b) first_variable\n(c) first-variable\nYour answer: ")
    if q5.lower() == 'b':
        print("✅ Correct!\n")
        score += 1
    else:
        print("❌ Incorrect. The correct answer is (b) first_variable.\n")
    # Final Score
    print(f"🎉 Your final score is {score} out of 5.\n")
    if score == 5:
        print("🥳 Perfect! You're a pro!")
    elif score == 4:
        print("😎 Good job!")
    elif score == 3:
        print("🙂 Not bad, but you can do better!")
    elif score == 2:
        print("😐 You might want to brush up on your knowledge.")
    elif score == 1:
        print("😕 Keep trying, you'll get there!")
    elif score == 0:
        print("😢 Don't be discouraged, every expert was once a beginner!")
    # Thank you message
    print("Thank you for playing the Ultimate Quiz by Prince Pathak! 🎉")
    # End of the quiz
    print("I hope you enjoyed it. Stay curious and keep learning! 🌟")

    again = input("\nWanna play again? (y/n): ")
    if again.lower() != 'y':
        print("Thanks for playing champ! 💖")
        break
