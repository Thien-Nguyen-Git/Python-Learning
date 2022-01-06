# ----------------------------------------------
# Date Example
# day_hours = 24
# week_days = 7

# week_hours = day_hours * week_days

# print(week_hours)
# ----------------------------------------------



# ----------------------------------------------
# Value Declaration
# x = 10
# y = "10"
# z = 10.1

# sum1 = x + x
# sum2 = y + y

# print(sum1, sum2)
# print(type(x), type(y), type(z))
# ----------------------------------------------



# ----------------------------------------------
# Example 1: 
# creating list using range
# list(rant(1, 10))
# Output
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example 2:
# using range with a 3rd argument
# list(rant(1, 10, 2))
# Output
# [1, 3, 5, 7, 9]
# happens every 2 item
# ----------------------------------------------



# ----------------------------------------------
# Example of Dictionary
# student_grades = [9.1, 8.8, 7.5]
# student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

# mysum = sum(student_grades.values())
# length = len(student_grades)
# mean = mysum / length
# print(mean)
# ----------------------------------------------



# ----------------------------------------------
# Example of Tuple
# monday_temperatures = (1, 4, 5)
# print(monday_temperatures)
# monday_temperatures = [9.1, 8.8, 7.5]
# monday_temperatures = ['hello', 1, 2, 3]
# ----------------------------------------------



# ----------------------------------------------
# Example of Function
# def mean(value):
#     if type(value) == dict:
#         the_mean = sum(value.values()) / len(value)
#     else:
#         the_mean = sum(value) / len(value)

#     return the_mean

# monday_temperatures = [8.8, 9.1, 9.9]
# student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}
# print(mean(student_grades))
# print(mean(monday_temperatures))
# ----------------------------------------------



# ----------------------------------------------
# Input

# Print Input of values
# def weather_condition(temperature):
#     if temperature > 7:
#         return "Warm"
#     else:
#         return "Cold"

# user_input = float(input("Enter temperature:"))
# print(weather_condition(user_input))

# user_input = input("Enter temperature:")
# print(type(user_input), user_input)


# Print Input of string
# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# when = "today"

# message1 = "Hello %s %s!" % (name, surname)
# message2 = f"Hello {name} {surname}. What's up {when}"
# print(message1)
# print(message2)
# ----------------------------------------------



# ----------------------------------------------
# Loops
# monday_temperatures = [9.1, 8.8, 7.6]

# print(round(monday_temperatures[0]))
# print(round(monday_temperatures[1]))
# print(round(monday_temperatures[2]))

# for temperature in monday_temperatures:
#     print(round(temperature))
#     print("Done")

# for letter in 'hello':
#     print(letter.title())



# Loop Dictionary
# student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

# for grades in student_grades.items():
#     print(grades)



# While Loop
# for i in [1,2,3]:
#     print(i)


# username = ''
# while username != "pypy":
#     username = input("Enter username: ")


# a = 0
# while a < 5:
#     a = a + 1
#     print(a)


while True:
    username = input("Enter username: ")
    if username == 'pypy':
        break
    else:
        continue
# ----------------------------------------------



















