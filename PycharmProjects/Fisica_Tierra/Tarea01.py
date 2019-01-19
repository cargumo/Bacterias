from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

## Tarea 1 Fisica de la Tierra

data = np.loadtxt('Para_Tarea1.txt')

z = data[:,0] # profundidad en km
rho = data[:,1] # densidad en gr/cc

# parametros
R = 6371
G = 6.6732*10**(-11)

# se cambian las unidades de la densidad a kg/m3
rho = rho*1000

# se cambia profundidad a radio
r = R - z # distancia al centro de la Tierra
# se cambian las unidades de km a m
r = r*1000

# se iterpolan los valores de densidades para r
f2 = interp1d(r, rho, kind='nearest')
r_new = np.arange(0,R)*1000
rho_new = f2(r_new)  # funcion de densidades para r


plt.plot(r,rho, 'o-')
plt.plot(r_new,rho_new, label='Interpolacion de los datos')
plt.title("Perfil de Densidades del Interior de la Tierra", fontsize=13)
plt.xlabel("Radio [km]", fontsize = 12)
plt.ylabel("Densidad [$gr/cm^3$]", fontsize=12)
plt.savefig("Perfil_de_Densidades_con_Ajuste")
plt.legend()
plt.show()


# Calcular la masa m(r)
# se integra la densidad en el volumen
masa = np.zeros(len(rho_new))
m_r = 0
for i in range(1,len(r_new)):
    m_r += (4*np.pi/3)*(r_new[i]**3 - r_new[i-1]**3)*rho_new[i]
    masa[i] = m_r

plt.plot(r_new, masa)
plt.plot(r_new[len(r_new)-1], masa[len(r_new)-1], 'o', label='Masa Total = $5.973x10^{24} [kg]$')
plt.title("Perfil de Masa de la Tierra en Funcion del Radio", fontsize=13)
plt.xlabel("Radio [m]", fontsize=12)
plt.ylabel("Masa [kg]", fontsize=12)
plt.savefig("Masa_Tierra_vs_r")
plt.legend()
plt.show()

print "Masa Total de la Tierra: ", masa[len(r_new)-1] # Masa Total de la Tierra

# Calcular la aceleracion de gravedad g(r)
g = np.zeros(len(rho_new))
for i in range(len(r_new)):
    g_r = G*masa[i]/(r_new[i]**2)
    g[i] = g_r

plt.plot(r_new, g)
plt.plot(r_new[len(r_new)-1], g[len(r_new)-1], 'o', label='$g$ en la superficie = $9.82 [m/s^2]$')
plt.title("Perfil de Gravedad al Interior de la Tierra", fontsize=13)
plt.xlabel("Radio [m]", fontsize=12)
plt.ylabel("Aceleracion de Gravedad [$m/s^2$]", fontsize=12)
plt.legend()
plt.savefig("g_vs_r")
plt.show()

print "Aceleracion de Gravedad en la Superficie: ", g[len(r_new)-1] # Masa Total de la Tierra
