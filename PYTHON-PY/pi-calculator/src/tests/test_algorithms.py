import unittest
from algorithms.leibniz import calculate_leibniz
from algorithms.monte_carlo import calculate_monte_carlo

class TestAlgorithms(unittest.TestCase):

    def test_calculate_leibniz(self):
        pi_value = calculate_leibniz()
        self.assertAlmostEqual(pi_value, 3.14159, places=5)

    def test_calculate_monte_carlo(self):
        pi_value = calculate_monte_carlo()
        self.assertAlmostEqual(pi_value, 3.14159, places=5)

if __name__ == '__main__':
    unittest.main()