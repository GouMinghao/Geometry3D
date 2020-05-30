#!/usr/bin/python
import unittest
loader = unittest.TestLoader()
tests = loader.discover("unit_tests", "test*.py")
runner = unittest.TextTestRunner(verbosity=2)
runner.run(tests)

