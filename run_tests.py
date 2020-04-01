#!/usr/bin/python
import unittest
loader = unittest.TestLoader()
tests = loader.discover("test", "test*.py")
runner = unittest.TextTestRunner(verbosity=2)
runner.run(tests)
