import matplotlib.pyplot as plt
import numpy as np

x = []
y = []

numb = [3]#,2,3,4,5,6]

for a in numb:
    data = np.loadtxt("C:/Users/vasob/OneDrive/Documents/FP/P07/FP_NV/fpi_cal/cal_" + str(a) + ".txt", delimiter="/", skiprows=0)
    for numbers in data:
        y.append(numbers[0])
        x.append(numbers[1])
    plt.plot(x,y, marker = "x", linestyle = "")
plt.show()