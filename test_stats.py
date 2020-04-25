###All that this script really does is plug data into scipy.
###Mostly here so that I can keep track of which test is which

import scipy.stats as stats
import sys
import numpy as np
import unittest
import mass

def t_test(mean , A , B = None):
	
	'''
	Takes in an array or list A and a mean to compare to.
	Tests to see if the given mean is consistent with A
	Performes a t - test to determine if the provided data is consistent with the given mean
	returns a t - value and a p - value
	You can also provie a second array B, in which case we will take the differences of all the elements. and compare that to the mean
	###I've been playing with this to see if two data sets are the same or not. Not yet convinced of how well it works
	
	'''
	if type(B) != type([0 , 0 ]):
		t , p = stats.ttest_1samp(A, mean)
		return t , p
	else:
		C = []
		if len(A) != len(B):
			print ("Error: Input lists are not the same size")
			sys.exit()
		else:
			for i in range(len(A)):
				C.append(A[i] - B[i])
		t , p = stats.ttest_1samp(A, mean)
	return t , p

def ks_test(A , B):
	'''
	Takes in two arrays A and B, then runs a two sided ks test on them.
	This test is used to determine if your two samples came from the same distribution.
	Note that this requires the same mean and variance
	returns a ks statistic and a p value
	'''
	
	ks , p = stats.ks_2samp(A , B)
	return ks , p
	

