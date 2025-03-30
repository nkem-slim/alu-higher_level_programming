#!/usr/bin/python3
"""
This module contains one function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounding to 2 decimal places.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers or floats.
        div (int or float): The divisor.

    Returns:
        list: A new matrix with the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix is not the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if any(not all(isinstance(num, (int, float)) for num in row)
           for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
