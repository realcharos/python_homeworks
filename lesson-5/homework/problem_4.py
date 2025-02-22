def enrollment_stats(universities):
    students = [uni[1] for uni in universities]
    tuition = [uni[2] for uni in universities]
    return students, tuition

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_numbers = sorted(numbers)
    mid = len(sorted_numbers) // 2
    return (sorted_numbers[mid] if len(sorted_numbers) % 2 != 0
            else (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2)

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

students, tuition = enrollment_stats(universities)

print("******************************")
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(tuition):,}")
print("")
print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,.2f}")
print("")
print(f"Tuition mean: $ {mean(tuition):,.2f}")
print(f"Tuition median: $ {median(tuition):,.2f}")
print("******************************")