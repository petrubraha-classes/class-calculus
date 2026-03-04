def tan_cont_frac (input: float) -> float:
    """Return an approximation of tan(input) using continuous functions, i.e. first method."""
    raise NotImplementedError("Exercitiul 3: tan_cont_frac nu a fost implementata")
    return input * (105 + 10 * input ** 2) / (105 - 35 * input ** 2)

def tan_poly_approx (input: float) -> float:
    """Return an approximation of tan(input) using a polynomial expansion, i.e. second method."""
    raise NotImplementedError("Exercitiul 3: tan_poly_approx nu a fost implementata")
    return input + (input ** 3) / 3 + (2 * input ** 5) / 15 + (17 * input ** 7) / 315
