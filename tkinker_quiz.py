import tkinter as tk
from tkinter import messagebox
import time


# QUIZ DATA
questions = [
    'What is the boiling point of water at sea level?',
    "Which gas do plants absorb during photosynthesis?",
    'What is the closest planet to the Sun?',
    'What is the chemical symbol for water?',
    'Which part of the human body pumps blood?',
    'What force pulls objects toward the Earth?',
    'Which of these is NOT a state of matter?',
    'What do bees collect from flowers?',
    'What is the largest planet in our solar system?',
    'What type of energy comes from the Sun?'
]

options = [
    ['50°C', '75°C', '100°C', '150°C'],
    ['CO₂', 'Nitrogen', 'Oxygen', 'Hydrogen'],
    ['Venus', 'Mars', 'Earth', 'Mercury'],
    ['CO₂', 'H₂O', 'O₂', 'NaCl'],
    ['Heart', 'Liver', 'Kidney', 'Lungs'],
    ['Magnetism', 'Electricity', 'Gravity', 'Friction'],
    ['Solid', 'Liquid', 'Gas', 'Light'],
    ['Stone', 'Pollen', 'Metal', 'Sand'],
    ['Earth', 'Jupiter', 'Mars', 'Saturn'],
    ['Solar energy', 'Wind energy', 'Chemical energy', 'Hydro energy']
]

answers = [
    '100°C', 'CO₂', 'Mercury', 'H₂O', 'Heart',
    'Gravity', 'Light', 'Pollen', 'Jupiter', 'Solar energy'
]

# -----------------------
# LOGIC
# -----------------------
current_q = 0
score = 0


def start_quiz():
    menu_frame.pack_forget()     # hide start menu
    quiz_frame.pack()            # show quiz
    load_question()


def load_question():
    question_label.config(text=f"Q{current_q+1}: {questions[current_q]}")

    for i in range(4):
        option_buttons[i].config(
            text=options[current_q][i],
            bg="white",
            state="normal"
        )


def check_answer(choice_index):
    global current_q, score

    selected = options[current_q][choice_index]
    correct = answers[current_q]

    # Disable buttons 
    for btn in option_buttons:
        btn.config(state="disabled")

    # Color effect
    if selected == correct:
        option_buttons[choice_index].config(bg="#4CAF50")   # green
        score += 1
    else:
        option_buttons[choice_index].config(bg="#E53935")   # red

        # highlight correct answer in green
        correct_index = options[current_q].index(correct)
        option_buttons[correct_index].config(bg="#4CAF50")

    # Move to next question after delay
    quiz_frame.after(1000, next_question)


def next_question():
    global current_q

    current_q += 1
    if current_q >= len(questions):
        show_final_score()
    else:
        load_question()


def show_final_score():
    messagebox.showinfo("Quiz Completed", f"Your Score: {score}/{len(questions)}")
    root.destroy()



# GUI SETUP

root = tk.Tk()
root.title("Science Quiz")
root.geometry("550x420")
root.config(bg="#f3f3f3")

# START MENU SCREEN

menu_frame = tk.Frame(root, bg="#f3f3f3")
menu_frame.pack(expand=True)

title = tk.Label(menu_frame, text="SCIENCE QUIZ", font=("Arial", 30, "bold"), bg="#f3f3f3", fg="#1a73e8")
title.pack(pady=30)

start_btn = tk.Button(
    menu_frame,
    text="Start Quiz",
    font=("Arial", 18, "bold"),
    bg="#1a73e8",
    fg="white",
    width=15,
    height=1,
    command=start_quiz
)
start_btn.pack(pady=20)


# QUIZ SCREEN

quiz_frame = tk.Frame(root, bg="#f3f3f3")

question_label = tk.Label(quiz_frame, text="", font=("Arial", 18), bg="#f3f3f3")
question_label.pack(pady=20)

option_buttons = []
for i in range(4):
    btn = tk.Button(
        quiz_frame,
        text="",
        font=("Arial", 14),
        width=30,
        height=1,
        bg="white",
        command=lambda i=i: check_answer(i)
    )
    btn.pack(pady=5)
    option_buttons.append(btn)

root.mainloop()
