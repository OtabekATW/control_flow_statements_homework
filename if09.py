def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number,    return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """

    x1 = a % 10
    x2 = a // 10
    y = x1 * 10 + x2

    if y <= a:
        s = True 
    if y >= a:
        s = False

    return s