###This script will check to make sure that the code is doing something sensible.
import unittest
import test_stats as test
import numpy as np
np.random.seed(42) ##Makes sure the test will give you the same results every time
		
class Test(unittest.TestCase):

	def test_t(self):
		###Should yield high p value
		A = np.random.normal( 0 , 1 , 100000)
		t , p = test.t_test(0 , A)
		#print (np.mean(A) , t , p)
		self.assertGreater(p , 0.05)
		
	
	def test_t_fail(self):
		###should yield low p value
		A = np.random.normal( 0 , 1 , 100000)
		t , p = test.t_test(1 , A)
		#print (np.mean(A) , t , p)
		self.assertGreater(.05 , p)
		
	def test_ks_test(self):
		###Should yield high p value
		A = np.random.normal( 0 , 1 , 100000)
		B = np.random.normal( 0 , 1 , 100000)
		t , p = test.ks_test(A , B)
		self.assertGreater(p , 0.05)
		
		
	def test_ks_test_diffmean(self):
		###Should yield low p value
		A = np.random.normal( 1 , 1 , 100000)
		B = np.random.normal( 0 , 1 , 100000)
		t , p = test.ks_test(A , B)
		self.assertGreater(.05 , p)
		
	def test_ks_test_diffvar(self):
		###Should yield low p value
		A = np.random.normal( 1 , 1 , 100000)
		B = np.random.normal( 1 , 2 , 100000)
		t , p = test.ks_test(A , B)
		self.assertGreater(.05 , p)
	
unittest.main()

