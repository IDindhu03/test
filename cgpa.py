def calculate_cgpa(grades):
    total_points = 0
    total_credits = 0
    
    for grade, credit in grades:
        total_points += grade * credit
        total_credits += credit
    
    cgpa = total_points / total_credits
    return cgpa

# Example usage:
# List of tuples where each tuple contains (grade, credit)
grades = [(9, 4), (8, 3), (7, 3), (10, 4), (6, 2)]

cgpa = calculate_cgpa(grades)
print(f"Your CGPA is: {cgpa:.2f}")
