# python3
# Data Structures with python3
counter = 0


def print_count(text):
    global counter
    counter += 1
    print(f"Prog No {counter} ---{text}")


"""
This program counts the outputs
GPA calculator

points = {"A+": 4.0, "A": 4, "A-": 3.67, "B+": 3.33, "B": 3.0}
num_courses = 0
total_points = 0
done = False
while not done:
    grade = input()
    if grade == "":
        break
    elif grade not in points:
        print("unknown grade '{0} being ignored".format(grade))
    else:
        num_courses += 1
        total_points += points[grade]
    if num_courses > 0:
        print("Your GPS is {0:.3}".format(total_points / num_courses))

print_count("input output")
# year = int(input("In what year you were born?"))
# reply = input("Enter x and y,separated by spaces:")
# pieces = reply.split()
# x = float(pieces[0])
# print(year)
# print(x)
#
print_count("age calculator with exceptions")

age = -1
while age <= 0:
    try:
        age = int(input("Enter your age in years:"))
        if age <= 0:
            print("your age must be positive")
    except (ValueError, EOFError):
        # print("Invalid response")
        pass

cars = ["bmw", "audi", "toyota", "subaru"]
# print(cars)
cars.reverse()
# print(cars)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# squares = [value**2 for value in range(1, 11)]
# print(min(digits), max(digits), sum(digits), sep=",")
# print(squares)

for i in range(1, 20):
    print(i)
digits = [value for value in range(1, 1000001)]
print(min(digits), max(digits), sum(digits), sep=",")
print([value for value in range(3, 30, 3)])
print([value for value in range(1, 20, 2)])
print([value**3 for value in range(1, 10)])
"""

digits = [value for value in range(1, 10)]
digituple = (100, 200, 50)
print(digituple)
for digit in digituple:
    print(digit)
