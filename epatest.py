import numpy as np

# Load data
# file = "uddscol.txt"
file = "hwycol.txt"

print("Tes file: "+ file)
raw = np.loadtxt(file, skiprows=2)

# Convert into sonething useful
t = raw[:, 0] # s
v = raw[:, 1]*0.447 #Convert mph to m/s

# Work out useful params
print("v_mean: " + str(np.mean(v)))

a = np.gradient(v, t)
P = a*v #vassuming mass of 1kg

print("P_max: " +str(np.max(P)))
print("v@P_max: " + str(v[np.argmax(P)]))

dt = t[1]
E_accel = np.sum(np.where(P>0, P, 0*P)*dt)
   # Extracts only matching  P

print("E_accel: " + str(E_accel))

v_rms = np.sqrt(np.mean(v**2))
print("v_rms: " + str(v_rms))

