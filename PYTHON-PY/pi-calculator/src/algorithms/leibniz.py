def calculate_leibniz(terms: int) -> float:
    pi_over_4 = 0.0
    for k in range(terms):
        pi_over_4 += ((-1) ** k) / (2 * k + 1)
    return pi_over_4 * 4