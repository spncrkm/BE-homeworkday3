#Lesson 4 Python Loop Statements
# Problem 1
# Task 1
import random
day_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
mood = ["Happy", "Sad", "Energetic", "Calm"]
for i in range(len(day_of_week)):
    print(f"{day_of_week[i]}, feels like {random.choice(mood)}")


# Problem 2
# Task 1

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
time_of_day = ["morning", "afternoon", "evening"]
for day in week:
    for time in time_of_day:
        print(f"This {day} at this {time} I felt {random.choice(mood)}")
