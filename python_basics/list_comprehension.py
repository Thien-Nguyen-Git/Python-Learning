# ----------------------------------------------
# temps = [221, 234, 340, 230]

# new_temps = []
# for temp in temps:
#     new_temps.append(temp / 10)

# print(new_temps)
# ----------------------------------------------



# ----------------------------------------------
# List Comprehension
# temps = [221, 234, 340, 230]

# new_temps = [temp / 10 for temp in temps]

# print(new_temps)
# ----------------------------------------------



# ----------------------------------------------
# List Comprehension
temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print(new_temps)
# ----------------------------------------------




