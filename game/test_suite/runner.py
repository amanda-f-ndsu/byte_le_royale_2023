import unittest
import game.test_suite.tests
    
if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = loader.discover('.')
    testRunner = unittest.TextTestRunner()
    test_results = testRunner.run(tests)

    if test_results.wasSuccessful(): 
        exit(0)
    else:
        exit(1)

# To run the test suite, make sure your terminal is in the root directory of the project (the 'byte_le_royale_2021 folder)
# Then, in your terminal, run 'python -m game.test_suite.runner'. This runs this file as a module of the entire project, allowing imports to function properly