import math


def factorial(n):
    """Calcular el factorial de un número n

    Args:
        n (int): integer

    Returns:
        int : factorial del número n

    Examples:

    >>> factorial(5)
    120

    >>> factorial(3)
    6

    >>> factorial(6-3)
    6
    """
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f


def combinaciones(n, r):
    """ Calcula las posibles combinacioens r en n
    basados en la formula de la combinatoria.


    Args:
        n (int): integer, n >= n
        r (int): integer, n <= r

    Returns:
        int : retorna el numero de combinaciones

    Examples:
    >>> combinaciones(3, 2)
    3

    >>> combinaciones(8, 5)
    56
    """
    fn = factorial(n)
    fr = factorial(r)

    fnr = factorial(n-r)

    # numero de combinaciones
    nc = fn // fr // fnr

    return nc


def es_primo(n):
    """determina si un númeor es primo o no

    Args:
        n (int): integer

    Returns:
        boolean : True or False

    Examples:

    >>> es_primo(5)
    True

    >>> es_primo(9)
    False

    >>> es_primo(2)
    True
    """
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def comienza_con(x):
    """determina el digito con el que inicia un numeor

    Args:
        x (int): integer

    Returns:
        int: integer

    Examples:
    >>> comienza_con(275)
    2
    >>> comienza_con(73949)
    7
    """
    pd = x
    while pd > 9:
        pd = pd // 10
    return pd


def mcd(x, y):
    """retorna el maximo comun divisor de x y y

    Args:
        x (int): integer
        y (int): integer

    Returns:
        int : integer

    Examples:
    >>> mcd(18, 24)
    6
    >>> mcd(7, 9)
    1
    """
    res = x % y
    while res != 0:
        x = y
        y = res
        res = x % y
    return y


def mcm(x, y):
    """retorna el minimo comun multiplo de x y y

    Args:
        x (int): integer
        y (int): integet

    Returns:
        int: integer

    Examples:

    >>> mcm(6, 12)
    12

    >>> mcm(13, 80)
    1040
    """
    return x*y//mcd(x, y)
