def addition(x: int, y: int) -> int:
    """Addition
    Args:
        x (int): Number 1
        y (int): Number 2

    Returns:
        int: Sum
    """
    z = x + y
    return z

def multiplication(x: int, y: int) -> int:
    """multiplication

    Args:
        x (int): Number 1
        y (int): Number 2

    Returns:
        int: int
    """
    return x * y

def division(x, y):
    """division

    Args:
        x (int): Number 1
        y (int): Number 2

    Returns:
        int: int
    """
    return x / y

def subtraction(x, y):
    """subtraction

    Args:
        x (int): Number 1
        y (int): Number 2

    Returns:
        int: int
    """
    return x - y


if __name__ == "__main__":
    # result should be 2005
    print(addition(200, 5))
