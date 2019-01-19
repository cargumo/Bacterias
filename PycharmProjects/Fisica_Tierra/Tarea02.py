from __future__ import division
import numpy as np
import matplotlib.pyplot as  plt
from scipy import special

'''Script para la Tarea 2 de fisica de la tierra'''

# Datos
Ts = 0  # temperatura de la superficie
Tm = 1450  # temperatura del manto
k = 3.318  # [J/Kms]
rho_m = 3330  # [kg/m3]  densidad del manto
Cp = 1.171 * 10**3  # [J/kgK]
kappa = k/(rho_m*Cp)
a = 95 * 10**3  # [m]  espesor asintotico
v = 6.6*10**(-2)/(3.15*10**7)  # [m/s]  velocidad de divergencia
R = v*a/(2*kappa)   # [-]  numero de Peclet

def Matos(a):
    Ma = a*10**6
    c = 3.15*10**7
    s = Ma*c
    return s

def stoMa(s):
    c = 3.15 * 10 ** 7
    a = s/c
    Ma = a/(10**6)
    return Ma

def T(z,t):
    eta = z/(2*np.sqrt(kappa*t))
    Temp = Ts + (Tm - Ts) * special.erf(eta)
    return Temp

# Parte c

# Para t = 16 Ma
t_1 = Matos(16)
prof = np.arange(0, 150, 0.1)*10**3  # [m]
temp16 = T(prof[:], t_1)
plt.plot(temp16, -prof*10**(-3))
plt.title("Temperatura en funcion de la profundidad para t=16Ma", fontsize=13)
plt.xlabel("Temperatura [C]", fontsize=11)
plt.ylabel("Profundidad [km]", fontsize=11)
plt.show()

# Para t = 45 Ma
t_2 = Matos(45)
prof = np.arange(0, 150, 0.1)*10**3  # [m]
temp45 = T(prof[:], t_2)
plt.plot(temp45, -prof*10**(-3))
plt.title("Temperatura en funcion de la profundidad para t=45Ma", fontsize=13)
plt.xlabel("Temperatura [C]", fontsize=11)
plt.ylabel("Profundidad [km]", fontsize=11)
plt.show()

# Grafico isotermas
# arreglo de edades
edades = np.arange(0.1,80, 1) # edades en Ma
edades = Matos(edades[:])  # edades en s
# arreglo de profundidades
prof = np.arange(0, 150, 1)*10**3  # profundiades en [m]

X, Y = np.meshgrid(edades, prof)
Z = T(Y,X)
cs = plt.contourf(stoMa(X[:]),-Y*10**(-3),Z, 7, cmap='plasma')
plt.clim(0, 1600)
plt.colorbar()
cont=plt.contour(cs, colors='k')
plt.clabel(cont, inline=1, fontsize=10)
plt.xlabel("Edad [Ma]",fontsize=11)
plt.ylabel("Profundidad [km]", fontsize=11)
plt.title("Estructura de Temperatura corteza oceanica Modelo semiespacio 1D", fontsize=13)
plt.show()

# Parte d

def T_gdh1(z, t):
    N = 10**3
    suma = 0
    for n in range(1,N):
        cn = 2/(n*np.pi)
        bn = np.sqrt(R**2 + n**2*np.pi**2) - R
        x = v*t
        suma += cn*np.exp(-bn*x/a)*np.sin(n*np.pi*z/a)
    t = Tm *(z/a + suma)
    return t

# Para t = 16 Ma
t_1 = Matos(16)
prof = np.arange(0, 150, 0.1)*10**3  # [m]
temp2 = T_gdh1(prof[:], t_1)
plt.plot(temp16, -prof*10**(-3), label='Modelo semiespacio 1D')
plt.plot(temp2, -prof*10**(-3), label='Modelo GDH1')
plt.title("Temperatura en funcion de la profundidad para t=16Ma", fontsize=13)
plt.xlabel("Temperatura [C]", fontsize=11)
plt.ylabel("Profundidad [km]", fontsize=11)
plt.legend()
plt.show()

# Para t = 45 Ma
t_2 = Matos(45)
prof = np.arange(0, 150, 0.1)*10**3  # [m]
temp2 = T_gdh1(prof[:], t_2)
plt.plot(temp45, -prof*10**(-3), label='Modelo semiespacio 1D')
plt.plot(temp2, -prof*10**(-3), label='Modelo GDH1')
plt.title("Temperatura en funcion de la profundidad para t=45Ma", fontsize=13)
plt.xlabel("Temperatura [C]", fontsize=11)
plt.ylabel("Profundidad [km]", fontsize=11)
plt.legend()
plt.show()

# Grafico isotermas
# arreglo de edades
edades = np.arange(0,80, 1) # edades en Ma
edades = Matos(edades[:])  # edades en s
# arreglo de profundidades
prof = np.arange(0, 150, 0.1)*10**3  # profundiades en [m]

X, Y = np.meshgrid(edades, prof)
Z = T_gdh1(Y,X)
cs = plt.contourf(stoMa(X[:]),-Y*10**(-3),Z, 8, cmap='plasma')
plt.clim(0, 1600)
plt.colorbar()
cont=plt.contour(cs, colors='k')
plt.clabel(cont, inline=1, fontsize=10)
plt.xlabel("Edad [Ma]", fontsize=11)
plt.ylabel("Profundidad [km]", fontsize=11)
plt.title("Estructura de Temperatura corteza oceanica Modelo GDH1", fontsize=13)
plt.show()