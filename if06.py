def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    s = 0

    if a > 0:
        s += 1

    if b > 0:
        s += 1

    if c > 0:
        s += 1

    if s > 1:
        d = 'there are a lot of positive numbers'

    if s == 0:
        d = 'there are a lot of negative numbers'   

    if s == 1:
        d = 'there are a lot of negative numbers'

    return d