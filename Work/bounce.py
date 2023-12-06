# bounce.py
#
# Exercise 1.5
height = 100
iteration = 1

while iteration <= 10:
    height = round((3/5)*height, 4)
    print(iteration, height)
    iteration = iteration + 1
