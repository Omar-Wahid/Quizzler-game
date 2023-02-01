from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

# false_img = PhotoImage(file="false.png")
# true_img = PhotoImage(file="true.png")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="score = 0", fg="White", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height= 250, bg="White")
        self.question_text = self.canvas.create_text(150, 125, text=f"random question",
                                                     width=280,
                                                     font=("Arial", 16, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.true = Button(text="True", font=("Arial", 18, "bold"), command=self.true_pressed)
        self.true.grid(column=0, row=2)

        self.false = Button(text="False", font=("Arial", 18, "bold"), command=self.false_pressed)
        self.false.grid(column=1, row=2)

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz is over")
            self.true.config(state="disabled")
            self.false.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
