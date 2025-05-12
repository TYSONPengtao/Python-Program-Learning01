# main.py

from algorithms.leibniz import calculate_leibniz
from algorithms.monte_carlo import calculate_monte_carlo

def main():
    leibniz_pi = calculate_leibniz()
    monte_carlo_pi = calculate_monte_carlo()

    print(f"Calculated Pi using Leibniz formula: {leibniz_pi}")
    print(f"Calculated Pi using Monte Carlo method: {monte_carlo_pi}")

if __name__ == "__main__":
    main()