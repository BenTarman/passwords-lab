import matplotlib.pyplot as plt

import numpy as np


x_axis = []
y_axis = []
colors = []

with open("q1Passwords.txt") as f:
    for data in f.readlines():
        data_line = data.strip().split()
        #print(data_line[1])
        y_axis.append(int(data_line[1]))

        passWordStrength = ""
        for i in range(2, len(data_line)):
            passWordStrength += data_line[i]
        passWordStrength = passWordStrength.strip()


        if (passWordStrength == "VeryWeak"):
            colors.append('red')
        elif (passWordStrength == "Weak"):
            colors.append('blue')
        elif (passWordStrength == "Good"):
            colors.append('green')
        elif (passWordStrength == "Strong"):
            colors.append('orange')
            print(data_line[1])
        elif (passWordStrength == "VeryStrong"):
            colors.append('brown')
        else:
            print(passWordStrength)


x_axis = list(range(len(y_axis)))

print(len(colors))
print(len(y_axis))

plt.scatter(x_axis, y_axis, s = 11, c = colors)
plt.xlabel('password index')
plt.ylabel('password strength')
plt.show()

