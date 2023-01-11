import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def Gauss(x, A, B, C):
    y = C*np.exp(-1*B*(x-A)**2)
    return y


currents = [5, 10, 15, 20, 40, 60, 80, 100, 120, 140, 160]
peaks = []
x = []
y = []
peaks_cw = []
fehler = []

data = np.loadtxt("C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/Spek-puls-RB/rot4-" + str(5) + "mA-puls.txt", delimiter="\t", skiprows=2)
for numbers in data:
    if (numbers[0] > 640 and numbers[0] < 670):
        x.append(numbers[0])
        y.append(numbers[1])
x = np.asarray(x)
y = np.asarray(y)

#parameters, covariance = curve_fit(Gauss, x, y, [670, 1, 43000])

#fehler = np.sqrt(np.diag(covariance))[0]
#print(parameters[0])
plt.rcParams.update({"font.family": "serif"})

plt.plot(x,y)
#plt.plot(x, Gauss(x,*parameters))
plt.legend()
plt.ylabel('Wellenlänge in nm', fontsize=16)
plt.xlabel('Strom in mA', fontsize=16)
plt.show()
#blau 450 473
#rot 5-40(640-670)(komplett für puls)  60-100(650-680)  120(660-685)  140(662-685, 670) 160(670-690, 680)
#lila-C (400-420) 410
#lila-L (400-412) 405