"""Basic arithmetic operations module."""

def add(a, b):
    """Return the sum of a and b."""
    return a + b


def sub(a, b):
    """Return the result of subtracting b from a."""
    return a - b


def mul(a, b):
    """Return the product of a and b."""
    return a * b


def div(a, b):
    """Return the result of dividing a by b.

    Raises:
        ValueError: If the divisor b is zero.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b
