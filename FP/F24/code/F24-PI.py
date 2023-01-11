import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.constants as sc
adiodes = []
bdiodes = []
cdiodes = []
ldiodes = ["lilaL", "lilaC", "lilaA", "lilaB"]
rdiodes = ["rot4"]
bdiodes = ["blau2"]
diode_arr = [rdiodes, bdiodes, ldiodes, cdiodes, adiodes, bdiodes]
puls_cw = ["puls", "cw"]
markers = ["o", "x", "^", "."]
v_labels = ["violett-C", "violett-L"]
diod_flache = [0.01, 0.09]

blaverage_puls = 464.30182357821235
blaverage_cw = 464.7805077076424

laverage_puls = 405.190587978064
laverage_cw = 406.3052185467753

caverage_puls = 411.17314134818906
caverage_cw = 411.54404074963827

redaverge_puls = 646.3567657680541
redaverge_cw = 648.0348202323783

wavelengths_puls = [caverage_puls, laverage_puls]
wavelengths_cw = [caverage_cw, laverage_cw]

x = []
y = []
P = []
empf_r = 0.36
empf_b = 0.23
empf_l = 0.17
empf_c = 0.18


empf_arr = [empf_r, empf_b, empf_l, empf_c]
empf_arr_lil = [empf_l, empf_c, 0.12, 0.12]

plt.rcParams.update({"font.family": "serif"})
fig, ax1 = plt.subplots(figsize=(8,6))
a = 0
i = 0
for led in ldiodes:
    data = np.loadtxt("C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/IUP-puls/" + led + "-IUP-puls.txt" , delimiter="\t" , skiprows=2, encoding = 'cp1252')
    for sets in data:
        x.append(sets[0]) # Strom
        y.append(sets[2]) # Photostrom
    x = np.asarray(x)
    y = np.asarray(y)

    P = np.divide(y, empf_arr_lil[i])
    perr = np.divide(y, empf_arr_lil[i]**2)*0.02
    plt.plot(x, P, marker = markers[i],linestyle='dashed',color= "m", label = led)
    #plt.errorbar(x,P, yerr= abs(perr), capsize= 4, ecolor = "black", barsabove= True, linestyle = "")
    i += 1
    x = list(x)
    y = list(y)
    x = []
    y = []

a = 3
i = 0
# for led in diode_arr[a]:
#     data = np.loadtxt("C:/Users/vasob/OneDrive/Documents/FP/F24/Nikolai-Vaso F24/IUP-puls/" + led + "-IUP-puls.txt" , delimiter="\t" , skiprows=2, encoding = 'cp1252')
#     for sets in data:
#         x.append(sets[0]) # Strom
#         y.append(sets[2]) # Photostrom
#     x = np.asarray(x)
#     y = np.asarray(y)

#     P = np.divide(y, empf_arr[a])
#     perr = np.divide(y, empf_arr[a]**2)*0.02
#     print(y)
#     plt.plot(x, P, marker = markers[i],linestyle='dashed',color= "m", label = led)
#     plt.errorbar(x,P, yerr= abs(perr), capsize= 4, ecolor = "black", barsabove= True, linestyle = "")
#     i += 1
#     x = list(x)
#     y = list(y)
#     x = []
#     y = []
    

plt.legend()
plt.xlabel('Strom I in A',fontsize=16)
plt.ylabel('Leistung P in W', fontsize=16)
plt.show()