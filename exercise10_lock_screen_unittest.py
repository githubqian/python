#!/usr/bin/env python


"""You are tasked with testing a lock screen pin pad for a smartphone.
We need you to create a test script that automates a test case where you set
the lock screen PIN, push the number buttons to unlock the device based on the
PIN, then ensure that the lock screen is unlocked.  This should be done with the
following PINs: 1234, 0000, 9999, 1470.  You can use the following APIs for the
lock screen below.  Feel free to add new APIs to this if needed."""



"""class LockScreen {
  void set_pin(int pin)
  void lock_device()
  boolean is_locked()
  void press_number(int number)
}"""
  
import unittest
import logging
import time
import LockScreen (???from class/file_name import function: e.g. from LockScreen import set_pin)
  
class TestLockScreenAPI(unittest.TestCase):
	
	log = logging.getLogger("TestLockScreenAPI.test_lock_screen_unlock")
	logging.basicConfig()
	log.setLevel(logging.INFO)
		
	def setUp(self):
		pins=[1234, 0000, 9999, 1470]
		lock_screen=LockScreen()
		#self.lock_screen=LockScreen(), then replace all the following lock_screen with self. lock_screen
		lock_screen.lock_device()
		#assert lock_screen.is_locked() == True
		self.assertTrue(lock_screen.is_locked())
		
	def tearDown(self):
		pins=[]
		lock_screen=None
		
	def test_lock_screen_unlock(self):

		for num in pins:
			lock_screen.set_pin(num)
			log.info("Pin is %d:" % num)
			lock_screen.press_number(num)
			time.sleep(2)
			#assert lock_screen.is_locked()==False
			self.assertFalse(lock_screen.is_locked())
			
if __name__ == '__main__':
    unittest.main()
			
			
"""if __name__ == "__main__":
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "TestLockScreenAPI.test_lock_screen_unlock" ).setLevel( logging.DEBUG )
    unittest.main()***
			
			
			
