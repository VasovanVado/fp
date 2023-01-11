import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


def Gauss(x, A, B, C):
    y = C*np.exp(-1*B*(x-A)**2)
    return y
i = 0
fehler_C = [0.9, 0.8, 0.5, 0.6, 1, 1.4, 2.3, 4, 4, 4, 4]
fehler_L = [0.8, 0.8, 0.6, 2, 2, 2, 3, 5, 5, 3, 4]
fehler_rot = [0.5, 0.5, 0.6, 1, 2, 3, 3, 4, 4, 5, 3]
fehler_blau = [0.5, 1, 0.5, 1.1, 2, 3, 2, 3, 4, 4, 4]

currents = [5, 10, 15, 20, 40, 60, 80, 100, 120, 140, 160]
blue_bounds = [450, 473]
rot_puls_bounds = [640, 670]
rot_cw_bounds = [[640, 670], [640, 670], [640, 670], [640, 670], [640, 670],[650, 680],[650, 680],[650, 680],[660,685],[662, 685], [670, 690]]
lila_C_bounds = [400, 420]
lila_L_bounds = [400, 412]
peaks = []
x = []
y = []
peaks_cw = []
fehler = []
plt.rcParams.update({"font.family": "serif"})
for mA in currents:
    data = np.loadtxt("C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/Spek-puls-lila/lila-L-" + str(mA) + "mA-puls.txt" , delimiter="\t" , skiprows=2)
    for numbers in data:
        if(numbers[0] > lila_L_bounds[0] and numbers[0] < lila_L_bounds[1]):
            x.append(numbers[0])
            y.append(numbers[1])
    x = np.asarray(x)
    y = np.asarray(y)
    y /= 1000
    parameters, covariance = curve_fit(Gauss, x, y, [405, 1, 50])
    
    fehler.append((np.sqrt(np.diag(covariance))[0]))
    peaks.append(parameters[0])
    
    x = []
    y = []
    x = list(x)
    y = list(y)
print(fehler)
plt.plot(currents, peaks, marker = 'o', label = "gepulste Wellenlängen Peaks", color = "red", linestyle = "dashed")
plt.errorbar(currents,peaks, xerr = fehler_blau, yerr=fehler, capsize= 4, ecolor = "black", barsabove= True, linestyle = "")
fehler = []
peaks = []
i = 0
for mA in currents:
    data = np.loadtxt("C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/Spek-cw-RB/rot4-" + str(mA) + "mA-cw.txt" , delimiter="\t" , skiprows=2)
    for numbers in data:
        if(numbers[0] > rot_cw_bounds[i][0] and numbers[0] < rot_cw_bounds[i][1]):
            x.append(numbers[0])
            y.append(numbers[1])
    x = np.asarray(x)
    y = np.asarray(y)
    y /= 1000
    parameters, covariance = curve_fit(Gauss, x, y, [rot_cw_bounds[i][0] + (rot_cw_bounds[i][1] - rot_cw_bounds[i][0])/2, 1, 43])
    i += 1
    fehler.append(np.sqrt(np.diag(covariance))[0])
    peaks.append(parameters[0])
    x = []
    y = []
    x = list(x)
    y = list(y)
plt.plot(currents, peaks, marker = 'x', label = "cw Wellenlängen Peaks", color = "red", linestyle = "solid")
plt.errorbar(currents,peaks, yerr = fehler, capsize= 4, ecolor = "black", barsabove= True, linestyle = "")
plt.legend()
plt.ylabel('Wellenlänge in nm', fontsize = 16)
plt.xlabel('Strom in mA', fontsize = 16)
plt.show()