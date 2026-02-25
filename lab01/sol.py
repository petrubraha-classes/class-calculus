UNIT = 1.0
"""Global float constant used internally."""

def find_machine_precision():
    """Returns the machine precision and the computed power (m)."""
    
    # The number of iterations = m = power.
    power = 0
    old_precision = 10
    machine_precision = 0.1
    
    while UNIT + machine_precision > UNIT:
        old_precision = machine_precision
        machine_precision /= 10
        power += 1

    # UNIT + old_precision / 10 == UNIT 
    return old_precision, power - 1

if __name__ == "__main__":
    machine_precision, power = find_machine_precision()
    print(f"Machine precision: {machine_precision}, m: {power}")
    print(f"First verification (should NOT be 1.0): {UNIT + machine_precision}")
    print(f"Second verification (should be 1.0): {UNIT + machine_precision / 10}")
