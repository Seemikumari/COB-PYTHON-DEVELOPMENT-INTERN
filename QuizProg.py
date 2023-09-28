import random

#  A list of 30 questions and their corresponding answers
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the capital of Japan?", "answer": "Tokyo"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "What is the largest mammal on Earth?", "answer": "Blue Whale"},
    {"question": "Who wrote the play 'Romeo and Juliet'?", "answer": "William Shakespeare"},
    {"question": "What is the chemical symbol for gold?", "answer": "Au"},
    {"question": "What is the powerhouse of the cell?", "answer": "Mitochondria"},
    {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
    {"question": "What is the national flower of England?", "answer": "Rose"},
    {"question": "What programming language is this quiz written in?", "answer": "Python"},
    {"question": "What is the freezing point of water in Celsius?", "answer": "0"},
    {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
    {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
    {"question": "What is the chemical symbol for water?", "answer": "H2O"},
    {"question": "What is the process of converting code into an executable program called?", "answer": "Compilation"},
    {"question": "Who was the first woman to fly solo across the Atlantic Ocean?", "answer": "Amelia Earhart"},
    {"question": "What is the largest organ in the human body?", "answer": "Skin"},
    {"question": "What is the capital of Australia?", "answer": "Canberra"},
    {"question": "What is the chemical symbol for oxygen?", "answer": "O"},
    {"question": "What is the speed of light?", "answer": "299,792,458 meters per second"},
    {"question": "Who is known as the 'Father of Computer Science'?", "answer": "Alan Turing"},
    {"question": "What is the chemical symbol for carbon dioxide?", "answer": "CO2"},
    {"question": "Who painted the 'Starry Night'?", "answer": "Vincent van Gogh"},
    {"question": "Who wrote the novel 'Pride and Prejudice'?", "answer": "Jane Austen"},
    {"question": "What is the currency of Japan?", "answer": "Japanese Yen"},
    {"question": "What is the largest organ in the human body?", "answer": "Skin"},
    {"question": "Who discovered penicillin?", "answer": "Alexander Fleming"},
    {"question": "What is the chemical symbol for sodium?", "answer": "Na"},
    {"question": "What is the process of splitting an atom called?", "answer": "Nuclear fission"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},

    # Add more questions here
]

def get_random_question():
    return random.choice(questions)

def ask_question(question):
    user_answer = input(question["question"] + " ")
    return user_answer.lower() == question["answer"].lower()

def main():
    random.shuffle(questions)  # Shuffle questions

    score = 0
    total_questions = len(questions)

    for i in range(total_questions):
        question = get_random_question()
        if ask_question(question):
            print("Sahi Jawab!!!!!")
            score += 1
        else:
            print(f"Wrong. The correct answer is: {question['answer']}")

    print(f"You got {score} out of {total_questions} questions correct!")

if __name__ == "__main__":
    main()
