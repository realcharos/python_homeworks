import csv
from collections import defaultdict

grades = defaultdict(list)
with open("grades.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        subject = row["Subject"]
        grade = int(row["Grade"])
        grades[subject].append(grade)

averages = {subject: sum(grades[subject]) / len(grades[subject]) for subject in grades}

with open("average_grades.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in averages.items():
        writer.writerow([subject, round(avg, 2)])

print("Average grades calculated and saved to average_grades.csv.")
