# List of all quiz questions
quizzes = [
    {
        "question": "What is the capital of France?",
        "options": ["A) London", "B) Berlin", "C) Paris", "D) Rome"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A) Tokyo", "B) Osaka", "C) Kyoto", "D) Yokohama"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["A) Sydney", "B) Canberra", "C) Melbourne", "D) Perth"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Canada?",
        "options": ["A) Toronto", "B) Montreal", "C) Ottawa", "D) Vancouver"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Germany?",
        "options": ["A) Hamburg", "B) Munich", "C) Frankfurt", "D) Berlin"],
        "answer": "D"
    },
    {
        "question": "What is the capital of Italy?",
        "options": ["A) Milan", "B) Naples", "C) Rome", "D) Venice"],
        "answer": "C"
    },
    {
        "question": "What is the capital of Spain?",
        "options": ["A) Barcelona", "B) Madrid", "C) Seville", "D) Bilbao"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Brazil?",
        "options": ["A) Brasilia", "B) Rio de Janeiro", "C) Sao Paulo", "D) Salvador"],
        "answer": "A"
    },
    {
        "question": "What is the capital of India?",
        "options": ["A) Mumbai", "B) New Delhi", "C) Kolkata", "D) Chennai"],
        "answer": "B"
    },
    {
        "question": "What is the capital of Russia?",
        "options": ["A) Yekaterinburg", "B) Saint Petersburg", "C) Novosibirsk", "D) Moscow"],
        "answer": "D"
    }
]

# Function to start the quiz
def start_quiz():

    print("\n===== Welcome To Quiz Game =====\n")

    # Get player name
    while True:
        name = input("\nEnter Player Name: ")
        if name != "":
            break
        print("\nName cannot be empty!")

    print(f"\nWelcome {name}!")

    # Variable to store total score
    score = 0

    # Loop through all questions
    for quiz in quizzes:

        print(f"\n{quiz['question']}")

        # Display all options
        for option in quiz["options"]:
            print(option)

        # Take valid answer only
        while True:
            answer = input("\nEnter Answer : ").upper()

            if answer in ["A", "B", "C", "D"]:
                break

            print("\nInvalid Option! Please Enter A, B, C or D")

        # Check answer
        if answer == quiz["answer"]:
            print("\nCorrect Answer!")
            score += 1
        else:
            print(f"\nWrong Answer! Correct Was {quiz['answer']}")

    # Display final score
    print(f"\nYour Score: {score}/{len(quizzes)}")

    # Display performance
    if score == 10:
        print("\nExcellent! You got all answers correct!")
    elif score >= 8:
        print("\nGood Job! You did well.")
    elif score >= 5:
        print("\nNice! You can do better.")
    else:
        print("\nBetter Luck Next Time!")

    # Ask user to play again
    play_again = input("\nDo you want to play again? (yes/no): ")

    if play_again.lower() == "yes":
        start_quiz()
    else:
        print("\nThanks For Playing!")

# Main menu function
def menu():

    while True:

        print("\n===== Main Menu =====")
        print("\n1. Start Quiz")
        print("2. Exit")

        choice = input("\nEnter Option : ")

        if choice == "1":
            start_quiz()
            break

        elif choice == "2":
            print("\nThanks For Playing!")
            break

        else:
            print("\nInvalid Choice! Please Enter 1 or 2.")

# Program starts from here
menu()