import tkinter as tk
from tkinter import messagebox
from grading import grading_scale


class GradingApp:
    def __init__(self, root):
        """
        Sets up the gui for the grading system
        """
        self.root = root
        self.root.title("Student Grading System")
        self.root.geometry("350x600")

        #Scrollable Frame
        self.canvas = tk.Canvas(self.root)
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        #Scroll Region
        self.scrollable_frame.bind("<Configure>", self.update_scroll_region)

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        #Student Data
        self.student_data = []

        #UI Components
        self.create_widgets()

    def update_scroll_region(self, event=None):
        """
        Updates the scroll of the canvas to include all widgets
        """
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def create_widgets(self):
        """
        Creates the widgets for the gui
        """
        #Label
        self.instruction_label = tk.Label(self.scrollable_frame, text="Enter the student's name and their scores", font=("Arial", 12))
        self.instruction_label.pack(pady=10)

        #Name
        self.name_label = tk.Label(self.scrollable_frame, text="Student Name:")
        self.name_label.pack(pady=5)

        self.name_entry = tk.Entry(self.scrollable_frame)
        self.name_entry.pack(pady=5)

        #Number of Scores
        self.num_scores_label = tk.Label(self.scrollable_frame, text="Number of Scores:")
        self.num_scores_label.pack(pady=5)

        self.num_scores_entry = tk.Entry(self.scrollable_frame)
        self.num_scores_entry.pack(pady=5)

        #Add Scores Button
        self.add_scores_button = tk.Button(self.scrollable_frame, text="Add Score Fields", command=self.add_score_fields)
        self.add_scores_button.pack(pady=10)

        #Submit Button
        self.submit_button = tk.Button(self.scrollable_frame, text="Submit", command=self.submit_data)
        self.submit_button.pack(pady=10)

        #Reset Button
        self.reset_button = tk.Button(self.scrollable_frame, text="Reset", command=self.reset_gui)
        self.reset_button.pack(pady=10)

        #Result
        self.result_label = tk.Label(self.scrollable_frame, text="Grades will be displayed here.", font=("Arial", 10), justify=tk.LEFT)
        self.result_label.pack(pady=10)

        #Store created labels and entries
        self.score_labels = []
        self.score_entries = []

    def add_score_fields(self):
        """
        Adds score inputs based on the number of scores
        """
        try:
            num_scores = int(self.num_scores_entry.get())
            if not (1 <= num_scores <= 10):
                messagebox.showwarning("Input Error", "Number of scores must be between 1 and 10.")
                return

            #Clear previous score fields
            self.clear_score_fields()

            for i in range(num_scores):
                label = tk.Label(self.scrollable_frame, text=f"Score {i + 1}:")
                label.pack(pady=5)
                entry = tk.Entry(self.scrollable_frame)
                entry.pack(pady=5)
                self.score_labels.append(label)
                self.score_entries.append(entry)

        except ValueError:
            messagebox.showwarning("Input Error", "Please enter a valid number for scores.")

    def submit_data(self):
        """
        Validates the user input, saves data to the txt file, averages grades, and displays the results
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

            #Save student data
            student_record = {
                "name": name,
                "scores": scores,
                "final_grade": final_grade}
            self.student_data.append(student_record)

            #Save to file
            with open("student_data.txt", "a") as file:
                file.write(f"Name: {name}, Scores: {scores}, Final Grade: {final_grade}\n")

            #Display result
            result_text = f"Student: {name}\nScores: {scores}\nFinal Grade: {final_grade}"
            self.result_label.config(text=result_text, fg="green")
            messagebox.showinfo("Success", "Student data submitted and saved successfully!")

        except Exception as e:
            messagebox.showerror("Unexpected Error", f"An error occurred: {e}")

    def reset_gui(self):
        """
        Resets the gui by clearing all input, scores, and results
        """
        #Clear name entry
        self.name_entry.delete(0, tk.END)

        #Clear number of scores entry
        self.num_scores_entry.delete(0, tk.END)

        #Clear score fields
        self.clear_score_fields()

        #Reset the result label
        self.result_label.config(text="Grades will be displayed here.", fg="black")

        #Clear student data
        self.student_data = []

    def clear_score_fields(self):
        """
        Clears all score fields (labels and entries)
        """
        for label in self.score_labels:
            label.destroy()
        for entry in self.score_entries:
            entry.destroy()
        self.score_labels = []
        self.score_entries = []


def run_app():
    """
    Completes the gui
    """
    root = tk.Tk()
    app = GradingApp(root)
    root.mainloop()
