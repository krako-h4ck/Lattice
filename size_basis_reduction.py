from utils import *
from gram_schmidt import *

def size_reduce(ordered_basis, gso_coefficients, i, j):
    if abs(gso_coefficients[i][j])>0.5:
        q = round(gso_coefficients[i][j])
        ordered_basis[i] = sub_list(ordered_basis[i], mult_list(q, ordered_basis[j]))
        for l in range(0, j+1):
            gso_coefficients[i][l] = gso_coefficients[i][l] - q*gso_coefficients[j][l]

    return ordered_basis, gso_coefficients

def size_basis_reduction(ordered_basis):
    _, gso_coefficients = gram_schmidt(ordered_basis)

    n = len(ordered_basis)
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            ordered_basis, gso_coefficients = size_reduce(ordered_basis, gso_coefficients, i, j)

    return ordered_basis, gso_coefficients


if __name__ == '__main__':
    test_ordered_basis = [[5, -3, -7], [2, -7, -7], [3, -10, 0]]

    size_reduced_basis, updated_gso_coefficients = size_basis_reduction(test_ordered_basis)

    print('size_reduced_basis=', size_reduced_basis)
    print('updated_gso_coefficients=', updated_gso_coefficients)