
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def tau(V):
	return 5.25e-10 * V ##Assumes units of km / 2

def integrate(times , I , V):
	integral = 0
	
	for i in range(len(times) - 1):
		t1 = times[i]
		t2 = times[i + 1]
		
		dt = t2 - t1
		
		I1 = I[i]
		I2 = I[i + 1]
		
		integral += dt * (I2 + I1) / 2.0 ##trapezoid rule
	
	return 2 *  integral / (V ** 2 * tau(V))
	
	

	
t1 = 0
t2 = 10 ##In some units

V = 10

times = range(20)
I = range(20)

A = integrate(times , I , V)

print (A)
