import random

# Define a list of 30 questions and their corresponding answers.
questions = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "How many continents are there on Earth?", "answer": "7"},
    {"question":"What is the currency of China?","answer":"Yuan"}
    {"question":"Who is the founder of the Red Cross?","answer":"Henri Dunant"}
    {"question":"When and where was the Red Cross established?","answer":"May 21, 1881, Washington, D.C."}
    {"question":"Which is the disease caused by hemoglobin deficiency? ","answer":"Anemia"}
    {"question":"","answerWho started making Qutub Minar?":"Qutub-ud-din aibak"}
    {"question":"Who was the founder of Banaras Hindu University? ","answer":"Madan Mohan Malviya"}
    {"question":"Who was the author of economics?","answer":"Chanakya (Kautilya)"}
    {"question":"Where is Vivekananda Memorial located?","answer":"Kanyakumari"}
    {"question":"Where is the headquarters of SAARC located?","answer":" Kathmandu, Nepal"}
    {"question":"How many countries are members of SAARC? ","answer":"8 (India, Nepal, Bangladesh, Sri Lanka, Maldives, Bhutan, Pakistan, Afghanistan)"}
    {"question":"Who built the Grant-Trunk Road?","answer":"Chandragupta Maurya"}
    {"question":"Which disease is caused by deficiency of Vitamin ‘B’? ","answer":"BeriBeri"}
    {"question":"Which disease is caused by deficiency of Vitamin ‘C’? ","answer":"Scurvy"}
    {"question":"Which disease is caused by deficiency of vitamin ‘D’? ","answer":"Rickets"}
    {"question":"Which vitamin deficiency does not cause blood clotting? ","answer":"Vitamin ‘K’"}
    {"question":"Which disease is caused by deficiency of Vitamin ‘E’? ","answer":"Infertility"}
    # Add more questions here
]

# Function to select a random question and get user input for an answer.
def random_quiz_question():
    question = random.choice(questions)
    print(question["question"])
    user_answer = input("Your answer: ").strip().lower()

    if user_answer == question["answer"].lower():
        print("Correct!")
    else:
        print(f"Wrong. The correct answer is {question['answer']}.")

# Main quiz loop
while True:
    input("Press Enter to start a new quiz or Ctrl+C to quit...")
    random_quiz_question()