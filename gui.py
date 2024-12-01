import tkinter as tk
from tkinter import messagebox
from grading import grading_scale

class GradingApp:
    def __init__(self, root):
        """
        Sets up the gui for the grading system.
        """
        self.root = root
        self.root.title("Student Grading System")
        self.root.geometry("800x600")

        # Student Scores Data
        self.student_data = []

        # UI Components
        self.create_widgets()

    def create_widgets(self):
        """
        Creates the widgets for the gui.
        """
        # Label
        self.instruction_label = tk.Label(self.root, text="Enter the student's name and their scores",
                                          font=("Arial", 12))
        self.instruction_label.pack(pady=10)

        # Name Entry
        self.name_label = tk.Label(self.root, text="Student Name:")
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack(pady=5)

        # Number of Scores Entry
        self.num_scores_label = tk.Label(self.root, text="Number of Scores:")
        self.num_scores_label.pack(pady=5)

        self.num_scores_entry = tk.Entry(self.root)
        self.num_scores_entry.pack(pady=5)

        # Add Scores Button
        self.add_scores_button = tk.Button(self.root, text="Add Score Fields", command=self.add_score_fields)
        self.add_scores_button.pack(pady=10)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_data)
        self.submit_button.pack(pady=10)

        # Result
        self.result_label = tk.Label(self.root, text="Grades will be displayed here.", font=("Arial", 10),
                                     justify=tk.LEFT)
        self.result_label.pack(pady=10)

    def add_score_fields(self):
        """
        Adds score inputs based on the number of scores.
        """
        try:
            num_scores = int(self.num_scores_entry.get())
            if not (1 <= num_scores <= 4):
                messagebox.showwarning("Input Error", "Number of scores must be between 1 and 4.")
                return

            # Clear any previous score fields
            if hasattr(self, "score_entries"):
                for entry in self.score_entries:
                    entry.destroy()

            self.score_entries = []
            for i in range(num_scores):
                label = tk.Label(self.root, text=f"Score {i + 1}:")
                label.pack(pady=5)
                entry = tk.Entry(self.root)
                entry.pack(pady=5)
                self.score_entries.append(entry)

        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid number for scores.")

    def submit_data(self):
        """
        Validates the input, computes grades, and displays the results.
        """
        try:
            name = self.name_entry.get().strip()
            if not name:
                messagebox.showwarning("Input Error", "Student name cannot be empty.")
                return

            scores = []
            for entry in self.score_entries:
                try:
                    score = int(entry.get())
                    if not (0 <= score <= 100):
                        messagebox.showwarning("Input Error", "Scores must be between 0 and 100.")
                        return
                    scores.append(score)
                except ValueError:
                    messagebox.showwarning("Input Error", "Please enter valid scores.")
                    return

            best_score = max(scores)
            final_grade = grading_scale(sum(scores) / len(scores), best_score)

            # Save student data
            self.student_data.append({
                "name": name,
                "scores": scores,
                "final_grade": final_grade
            })

            # Display result
            result_text = f"Student: {name}\nScores: {scores}\nFinal Grade: {final_grade}"
            self.result_label.config(text=result_text, fg="green")
            messagebox.showinfo("Success", "Student data submitted successfully!")

        except Exception as e:
            messagebox.showerror("Unexpected Error", f"An error occurred: {e}")

def run_app():
    """
    Initializes the gui application.
    """
    root = tk.Tk()
    app = GradingApp(root)
    root.mainloop()
