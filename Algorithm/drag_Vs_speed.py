import numpy as np
import matplotlib.pyplot as plt
rho = 1.225
v = np.linspace(0,100,100) #velocity in meter square
Cd = 0.21 #Drag coefficient
Area = 2.36   # in meter square
Fd = [0]*100 # drag coefficient
print(Fd)
j = 0
for i in v:
    #Drag force
    Fd[j] = 0.5*rho*(i**2)*Cd*Area
    j += 1

plt.plot(v, Fd)
plt.show()

