import numpy as np
import matplotlib.pyplot as plt
# Task 2: Change R and C values here to see the effect on the graph
R = 2000    
C = 1e-6     
V = 5        
# Calculate the Time Constant  
tau = R * C
print("Time Constant (tau):", tau, "seconds")
# Create time values from 0 to 0.01 seconds
t = np.linspace(0, 0.01, 1000)
# Task 1: Modify program for discharging capacitor
# Formula: Vc = V * e^(-t / RC)
Vc = V * np.exp(-t / (R * C))
# Plotting the graph
plt.plot(t, Vc, label="Voltage across Capacitor")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title(f"RC Discharging Curve (R={R}, C={C})")
plt.grid(True)
plt.legend()
plt.show()