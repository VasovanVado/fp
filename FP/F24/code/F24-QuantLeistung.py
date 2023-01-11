import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.constants as sc



cdiodes = ["lilaC",  "lilaB"]
ldiodes = ["lilaA", "lilaL"]
rdiodes = ["rot4"]
bdiodes = ["blau2"]
diode_arr = ["rot4", "blau2", "lilaL", "lilaC", "lilaA", "lilaB"]
puls_cw = ["puls", "cw"]
markers = ["o", "x", "^", "."]
v_labels = ["violett-C", "violett-L"]
diod_flache = [0, 0, 0.09, 0.01, 0.04, 0.02]

bl20mA_puls = 464.30182357821235
bl20mA_cw = 464.7805077076424

l20mA_puls = 405.190587978064
l20mA_cw = 406.3052185467753

c20mA_puls = 411.17314134818906
c20mA_cw = 411.54404074963827

red20mA_puls = 646.3567657680541
red20mA_cw = 648.0348202323783

wavelength20mA = [[red20mA_puls, red20mA_cw], [bl20mA_puls, bl20mA_cw], [l20mA_puls, l20mA_cw], [c20mA_puls, c20mA_cw], [345, 354], [335, 355]]

x = []
y = []
P = []
empf_r = 0.36
empf_bl = 0.23
empf_l = 0.17
empf_c = 0.18
empf_a = 0.12
empf_b = [0.12, 0.11]

empf_arr = [empf_r, empf_bl, empf_l, empf_c, empf_a]
color_arr = ["red", "blue", "m", "m", "m", "m"]
rb_desc = "Strom I in A"
lila_desc = "Stromdichte J in A/m$^2$"

plt.rcParams.update({"font.family": "serif"})
fig, ax1 = plt.subplots(figsize=(8,6))
a = 5
i = 0
for mode in puls_cw:
    data = np.loadtxt("C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/IUP-" + mode + "/" + diode_arr[a] + "-IUP-" + mode + ".txt" , delimiter="\t" , skiprows=2, encoding = 'cp1252')
    for sets in data:
        x.append(sets[0]) # Strom
        y.append(sets[2]) # Photostrom
    x = np.asarray(x)
    y = np.asarray(y)
    
    if(a != 5):
        P = np.divide(y, empf_arr[a])
        perr = np.divide(y, empf_arr[a]**2)*0.02
    if(a == 5):
        P = np.divide(y, empf_b[i])
        perr = np.divide(y, empf_b[i]**2)*0.02
    photons = P/(sc.Planck*(sc.speed_of_light/(wavelength20mA[a][i]*10**(-9))))
    electrons = (x)/sc.elementary_charge
    qeff = (photons)/(electrons)
    if(a > 1):
        x /= (diod_flache[a] * 10**(-6))

    qerr = perr/(sc.Planck*(sc.speed_of_light/(wavelength20mA[a][i]*10**(-9))))
    plt.plot(x, qeff, marker = markers[i],linestyle='',color= color_arr[a], label = mode)
    plt.errorbar(x,qeff, yerr= abs(perr), capsize= 4, ecolor = "black", barsabove=False, linestyle = "")
    i += 1
    x = list(x)
    y = list(y)
    x = []
    y = []
plt.legend()
if(a <= 1):
    plt.xlabel(rb_desc,fontsize=16)
if(a > 1):
    plt.xlabel(lila_desc,fontsize=16)
plt.ylabel('externe Quanteneffizienz $\eta_{ext}$', fontsize=16)
plt.show()