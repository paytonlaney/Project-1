import tkinter as tk
from tkinter import messagebox
from grading import grading_scale

class GradingApp:
    def __init__(self, root):
        """
        Sets the gui components for the grading system.
        """
        self.root = root
        self.root.title("Student Grading System")
        self.root.geometry("400x400")

        # Student Scores Data
        self.student_scores = []

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the gui.
        """
        # Label
        self.instruction_label = tk.Label(self.root, text="Enter the number of students and their scores",
                                          font=("Arial", 12))
        self.instruction_label.pack(pady=10)

        # Number of Students
        self.num_students_label = tk.Label(self.root, text="Number of Students:")
        self.num_students_label.pack(pady=5)

        self.num_students_entry = tk.Entry(self.root)
        self.num_students_entry.pack(pady=5)

        # Scores Entry
        self.scores_label = tk.Label(self.root, text="Enter Scores (space separated):")
        self.scores_label.pack(pady=5)

        self.scores_entry = tk.Entry(self.root)
        self.scores_entry.pack(pady=5)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_scores)
        self.submit_button.pack(pady=15)

        # Result
        self.result_label = tk.Label(self.root, text="Grades will be displayed here.", font=("Arial", 10),
                                     justify=tk.LEFT)
        self.result_label.pack(pady=10)

    def submit_scores(self):
        """
        Validates the input, retrieves the scores, and displays the grades.
        """
        try:
            num_students = int(self.num_students_entry.get())
            if num_students <= 0:
                messagebox.showwarning("Input Error", "Number of students must be a positive integer.")
                return

            # Validates the scores
            scores_input = self.scores_entry.get().split()
            if len(scores_input) != num_students:
                messagebox.showwarning("Input Error", f"Please enter exactly {num_students} scores.")
                return

            self.student_scores = [int(score) for score in scores_input]
            best_score = max(self.student_scores)

            # Generates grades for each student
            grades = []
            for index, score in enumerate(self.student_scores, 1):
                grade = grading_scale(score, best_score)
                grades.append(f"Student {index}: Score = {score}, Grade = {grade}")

            # Display the results
            self.result_label.config(text="\n".join(grades))

        except ValueError:
            messagebox.showwarning("Input Error", "Please enter valid integer values for scores.")


def run_app():
    """
    Gui app is initalized.
    """
    root = tk.Tk()
    app = GradingApp(root)
    root.mainloop()  # Keeps the window open


if __name__ == "__main__":
    run_app()
