import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        else:
            return None

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz")

        self.quiz = Quiz()

        # Add questions to the quiz
        self.quiz.add_question(Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"))
        self.quiz.add_question(Question("What is the largest planet in our Solar System?", ["Earth", "Jupiter", "Mars", "Venus"], "Jupiter"))
        self.quiz.add_question(Question("Which element does 'O' represent on the periodic table?", ["Oxygen", "Gold", "Silver", "Hydrogen"], "Oxygen"))

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.options_var = tk.StringVar(value=None)
        self.option_buttons = []
        for i in range(4):
            option_button = tk.Radiobutton(root, text="", variable=self.options_var, value="", font=("Arial", 12))
            self.option_buttons.append(option_button)
            option_button.pack(anchor="w")

        self.next_button = tk.Button(root, text="Next", command=self.check_answer, font=("Arial", 12))
        self.next_button.pack(pady=20)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 14))
        self.score_label.pack()

        self.load_next_question()

    def load_next_question(self):
        question = self.quiz.get_next_question()
        if question:
            self.question_label.config(text=question.prompt)
            self.options_var.set(None)
            for idx, option_button in enumerate(self.option_buttons):
                option_button.config(text=question.options[idx], value=question.options[idx])
        else:
            messagebox.showinfo("Quiz Completed", f"Your score is: {self.quiz.score}/{len(self.quiz.questions)}")
            self.root.quit()

    def check_answer(self):
        selected_option = self.options_var.get()
        current_question = self.quiz.questions[self.quiz.current_question_index - 1]
        if selected_option == current_question.answer:
            self.quiz.score += 1
        self.score_label.config(text=f"Score: {self.quiz.score}")
        self.load_next_question()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

