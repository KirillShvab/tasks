import unittest

if __name__ == '__main__':
    loader = unittest.TestLoader()
    runner = unittest.TextTestRunner(verbosity=2)

    suite_circle = loader.loadTestsFromName('test.test_circle')
    runner.run(suite_circle)

    suite_triangle = loader.loadTestsFromName('test.test_triangle')
    runner.run(suite_triangle)
