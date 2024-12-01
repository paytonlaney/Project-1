def grading_scale(student_score: float, best_score: int) -> str:
    """
    Determines the grade of a student based on their score.
    """
    if student_score >= best_score - 10:
        return 'A'
    elif student_score >= best_score - 20:
        return 'B'
    elif student_score >= best_score - 30:
        return 'C'
    elif student_score >= best_score - 40:
        return 'D'
    else:
        return 'F'

