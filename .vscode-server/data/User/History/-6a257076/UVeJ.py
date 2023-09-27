import numpy as np

##########################################################################
# Graded Functions
##########################################################################
# Define our global size variables.
n = 3
m = 2
k = 4

def multiply_with_loops(matrix1, matrix2):
    """
    :param matrix1: int array with dimensions N x M
    :param matrix2: int array with dimensions M x K
    :return: matrix1 * matrix2
    """
    # We will make our output array and make it of size N x K
    # because check_equal takes matrices of size N x K.
    output = [[0 for col in range(k)] for row in range(n)]

    # Now, we will multiply the values in both of the matricies and put them
    # in the output matrix.
    # The two outer loops are in range(n) and range(k) because matrix1 and matrix2
    # do not share those size values.
    for matrix1_row in range(n):
        for matrix2_col in range(k):
            # The innermost loop is in range(m) because both matrix1 and matrix2 share the
            # size value.
            for shared in range(m):
                output[matrix1_row][matrix2_col] = matrix1[matrix1_row][shared] * matrix2[shared][matrix2_col]
    return output

def multiply_with_numpy(matrix1, matrix2):
    """
    :param matrix1: int array with dimensions N x M
    :param matrix2: int array with dimensions M x K
    :return: matrix1 * matrix2
    """
    # We are using the built-in matmul function from numpy which does matrix
    # multiplication for us.
    # We do not even need to store it as a variable because we can simply return it.
    return np.matmul(matrix1, matrix2)

def check_equal(matrix1, matrix2) -> bool:
    """
    :param matrix1: int array with dimensions N x K
    :param matrix2: int array with dimensions N x K
    :return: bool
    """
    # As both matrix1 and matrix2 are of size N x K, we loop through all of the
    # rows (n) and columns (k) for both of the arrays.
    # If every value in matrix1 is equal to every value in matrix2 at the same
    # position, then we return True as the matrices are the same, else,
    # we return False.
    for row in range(n):
        for col in range(k):
            if matrix1[row][col] != matrix2[row][col]:
                return False
    return True

##########################################################################
# Main Script
##########################################################################
if __name__ == "__main__":
    # Create two matrices of random integers.
    matrix1 = np.random.randint(low=0, high=10000, size=(n, m))
    matrix2 = np.random.randint(low=0, high=10000, size=(m, k))

    # Now, we will input the two random matricies into our multiply matrix functions.
    output1 = multiply_with_loops(matrix1, matrix2)
    output2 = multiply_with_numpy(matrix1, matrix2)

    # Finally, we will check to see if both the multiply matrix functions output the same value and return it.
    print(check_equal(output1, output2))