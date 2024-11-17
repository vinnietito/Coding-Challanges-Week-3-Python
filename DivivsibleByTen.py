def divisible_by_ten(num):
    """
    Check if a number is divisible by 10.

    Args:
        num (int): The number to check.

    Returns:
        bool: True if divisible by 10, False otherwise.
    """
    
    if num % 10 == 0:
        return True
    else:
        return False
    
#Test Cases
print(divisible_by_ten(20)) #Output: True (20 is divisible by 10)
print(divisible_by_ten(23)) #Output: False (33 is not divisible by 10)
print(divisible_by_ten(50)) #Output: True (50 is didvisible by 10)
