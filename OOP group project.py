import time
import random

class QuizGame:
    def __init__(self):
        self.questions = [
            {
                'category': 'Science',
                'difficulty': 'Easy',
                'question': 'What is water called in its solid state?',
                'choices': ['stone', 'ice', 'frozen', 'water'],
                'correct_answer': 'ice'
            },
            {
                'category': 'Science',
                'difficulty': 'Medium',
                'question': 'What is the study of living organisms called?',
                'choices': ['Photosynthesis', 'folicle', 'Biology', 'physiology'],
                'correct_answer': 'Biology'
            },
            {
                'category': 'Science',
                'difficulty': 'Hard',
                'question': 'What is the largest planet in our solar system?',
                'choices': ['Jupiter', 'Venus', 'Mars', 'Earth'],
                'correct_answer': 'Jupiter'
            },
            {
                'category': 'Math',
                'difficulty': 'Easy',
                'question': 'How many millimeters are in a litre?',
                'choices': ['100', '500', '10000', '1000'],
                'correct_answer': '1000'
            },
            {
                'category': 'Math',
                'difficulty': 'Medium',
                'question': 'How many degrees are in a right angle?',
                'choices': ['9', '95', '90', '900'],
                'correct_answer': '90'
            },
            {
                'category': 'Math',
                'difficulty': 'Difficult',
                'question': 'How many edges does an octahedron have?',
                'choices': ['13', '12', '11', '10'],
                'correct_answer': '12'
            },
            {
                'category': 'History',
                'difficulty': 'Easy',
                'question': 'who led germany in World War 2?',
                'choices': ['Adolf Hitler', 'Karl Donitz', 'Joseph Stalin', 'Franklin Roosevelt'],
                'correct_answer': 'Adolf Hitler'
            },
            {
                'category': 'History',
                'difficulty': 'Medium',
                'question': 'When was the first computer invented?',
                'choices': ['1999', '1899', '1833', '2010'],
                'correct_answer': '1833'
            },
            {
                'category': 'History',
                'difficulty': 'Medium',
                'question': 'What is the name of the most famous pyramid?',
                'choices': ['Mars', 'Giza', 'Gaza', 'Pyr'],
                'correct_answer': 'Giza'
            },
            {
                'category': 'History',
                'difficulty': 'Hard',
                'question': 'Who invested the light bulb?',
                'choices': ['Thomas Edison', 'Methembe nyathi', 'Abner Doubleday', 'Shoniwa'],
                'correct_answer': 'Thomas Edison'
            }
            
        ]
        self.score = 0
        self.timer_duration = 10 # seconds

    def display_question(self, question):
        print(f"\nCategory: {question['category']}  |  Difficulty: {question['difficulty']}")
        print(question['question'])
        for i, choice in enumerate(question['choices'], start=1):
            print(f"{i}. {choice}")

    def get_user_answer(self):
        while True:
            try:
                user_input = int(input("Enter the number of your answer: "))
                if 1 <= user_input <= 4:
                    return user_input
                else:
                    print(" Please enter a number between 1 and 4.")
            except ValueError:
                print(" Please enter a number.")

    def run_quiz(self):
        print("Welcome to group 12's Quiz Game! You have 15 seconds to answer 10 questions in 3 categories. Science, Math and History")
        time.sleep(1)

        random.shuffle(self.questions) 

        for question in self.questions:
            self.display_question(question)

            start_time = time.time()
            user_answer = self.get_user_answer()
            end_time = time.time()

            elapsed_time = end_time - start_time

            if elapsed_time > self.timer_duration:
                print("You took too long to answer.")
            elif question['choices'][user_answer - 1] == question['correct_answer']:
                print("Correct!")
                self.score += 1
            else:
                print(f"Wrong! The correct answer is {question['correct_answer']}.")

            print(f"Your current score is: {self.score}")
            time.sleep(1)

        print("Quiz complete!")
        print(f"Your final score is: {self.score}")


if __name__ == "__main__":
    quiz_game = QuizGame()
    quiz_game.run_quiz()
