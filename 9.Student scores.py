import numpy as np
student_scores = np.array([
    [85, 90, 78, 92],
    [88, 76, 93, 85],
    [90, 88, 79, 94],
    [78, 85, 88, 80],
    [82, 91, 84, 86],
])
print("Student Scores:")
print(student_scores)
average_scores = student_scores.mean(axis=0)
print("\nAverage Scores for each Subject:")
print(f"Math: {average_scores[0]:.2f}, Science: {average_scores[1]:.2f}, English: {average_scores[2]:.2f}, History: {average_scores[3]:.2f}")
subjects = ['Math', 'Science', 'English', 'History']
highest_avg_score_index = np.argmax(average_scores)
highest_avg_score_subject = subjects[highest_avg_score_index]
print(f"\nSubject with the highest average score: {highest_avg_score_subject} with an average score of {average_scores[highest_avg_score_index]:.2f}")
