
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

tau0 = 0.002
def tau(V):
	return tau0

def integrate(times , I , V):
	integral = 0
	
	for i in range(len(times) - 1):
		t1 = times[i]
		t2 = times[i + 1]
		
		dt = t2 - t1
		
		I1 = I[i] / (V ** 2 * tau(V))
		I2 = I[i + 1] / (V ** 2 * tau(V))
		
		integral += dt * (I2 + I1) / 2.0 ##trapezoid rule
	
	return integral
	

	
t1 = 0
t2 = 10 ##In some units

V = 10

times = range(20)
I = range(20)

A = integrate(times , I , V)

print (A)
