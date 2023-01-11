import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

currents = [5, 10, 15, 20, 40, 60, 80, 100, 120, 140, 160]

fileDirs = [

    "C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/Spek-cw-Lila/lila-C-20mA-cw.txt",
    "C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/Spek-puls-Lila/lila-L-20mA-puls.txt",
    "C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/Spek-cw-RB/rot4-20mA-cw.txt",
    "C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/Spek-puls-RB/rot4-20mA-puls.txt",
    "C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/Spek-cw-RB/blau2-20mA-cw.txt",
    "C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/Spek-puls-RB/blau2-20mA-puls.txt",
    "C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/Spek-cw-RB/weiß-20mA-cw.txt",
]
colorName = [ ["cw Violett", "solid", "purple"], ["Puls Violett", "dashed", "purple"], [
    "cw Rot", "solid", "red"],  ["Puls Rot", "dashed", "red"], ["cw Blau", "solid", "blue"], ["Puls Blau", "dashed", "blue"], ["cw Weiß", "solid", "black"]]


x = []
y = []
i = 0
plt.rcParams.update({"font.family": "serif"})

for file in fileDirs:
    data = np.loadtxt(file, delimiter="\t", skiprows=2)
    for numbers in data:
        x.append(numbers[0])
        y.append(numbers[1])
    plt.plot(x, y, color=colorName[i][2],
             label=colorName[i][0], linestyle=colorName[i][1])
    i += 1
    x = []
    y = []

plt.legend()
plt.xlabel('Wellenlänge in nm')
plt.ylabel('Counts')
plt.show()
