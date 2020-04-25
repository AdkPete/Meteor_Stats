
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad


def tau(V):
	return 5.25e-10 * V ##Assumes units of km / 2

def integrate(times , I , V):

	'''
	times should be array-like, and contain the times of each brightness measurement.
	I contains the measured intensities at each time
	V should be the magnitude of the velocity of the meteor in km / s
	'''
	
	
	integral = 0
	
	for i in range(len(times) - 1):
		t1 = times[i]
		t2 = times[i + 1]
		
		dt = t2 - t1
		
		I1 = I[i]
		I2 = I[i + 1]
		
		integral += dt * (I2 + I1) / 2.0 ##trapezoid rule
	
	return 2 *  integral / (V ** 2 * tau(V)) , integral
	
	
def f(x):
	return x
	
x = np.array(range(100))
y = f(x)
v = 40

a , b = integrate(x , y , v)
print (b , b - 0.5 * max(x) * max(y))
