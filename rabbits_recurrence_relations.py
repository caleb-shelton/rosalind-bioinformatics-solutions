def fibonacci(n, k):
    """
    Given n, return the number of rabbit pairs that will be present after n months.
    k represents the number of offspring rabbit pairs after 1 month.
    """
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1, k) + k*fibonacci(n-2, k)
