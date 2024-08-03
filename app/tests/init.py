"""
Test Suite for Bored Cat Application

This package contains unit tests and integration tests for the Bored Cat application.
"""

import unittest

# Import test modules
from .test_main_window import TestMainWindow
from .test_menu import TestMenu
from .test_mouse_chase import TestMouseChase
from .test_laser_pointer import TestLaserPointer
from .test_fish_tank import TestFishTank
from .test_yarn_ball import TestYarnBall
from .test_style import TestStyle

def run_all_tests():
    """
    Run all tests in the test suite.
    """
    # Create a test suite
    test_suite = unittest.TestSuite()

    # Add test cases
    test_suite.addTest(unittest.makeSuite(TestMainWindow))
    test_suite.addTest(unittest.makeSuite(TestMenu))
    test_suite.addTest(unittest.makeSuite(TestMouseChase))
    test_suite.addTest(unittest.makeSuite(TestLaserPointer))
    test_suite.addTest(unittest.makeSuite(TestFishTank))
    test_suite.addTest(unittest.makeSuite(TestYarnBall))
    test_suite.addTest(unittest.makeSuite(TestStyle))

    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)

if __name__ == "__main__":
    run_all_tests()