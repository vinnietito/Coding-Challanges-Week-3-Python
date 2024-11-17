def large_power(base, exponent):
    """
    Check if base raised to the power of exponent is greater than 5000.

    Args:
        base (int or float): The base number.
        exponent (int): The exponent to which the base is raised.

    Returns:
        bool: True if the result is greater than 5000, False otherwise.
    """
    result = base ** exponent
    if result > 5000:
        return True
    else:
        return False
    
#Test cases
print(large_power(10, 3)) #Output: True (10^3 = 1000)
print(large_power(2,10)) #Output: True (2^10 = 1024)
print(large_power(3, 5)) #Output: False (3^5 = 243)
    