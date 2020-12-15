def square(n):
    """Return the square of a number"""
    return n ** 2

def triangle(n):
    """Triangulate a number"""
    res = 0
    for num in range(n + 1):
        res += num
    return res

def cube(n):
    """Return the cube of a number"""
    return n ** 3