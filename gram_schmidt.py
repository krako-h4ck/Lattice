from utils import *

def gram_schmidt(ordered_basis):
    n = len(ordered_basis)
    m = len(ordered_basis[0])

    gso_vectors = [[] for i in range(n)]
    gso_coefficients = [[0 for j in range(n)] for i in range(n)]

    for i in range(n):
        gso_vectors[i] = ordered_basis[i]
        gso_coefficients[i][i] = 1
        for j in range(i):
            coef = inner_product(ordered_basis[i], gso_vectors[j]) / inner_product(gso_vectors[j], gso_vectors[j])
            gso_coefficients[i][j] = coef
            gso_vectors[i] = [x-y for x,y in zip(gso_vectors[i], mult_list(gso_vectors[j], coef))]

    return gso_vectors, gso_coefficients


if __name__ == '__main__':
    test_ordered_basis = [[-1, -2, 3, 1], [-6, -4, 5, 1], [5, 5, 1, -3]]

    gso_vectors, gso_coefficients = gram_schmidt(test_ordered_basis)

    print('gso_vectors=', gso_vectors)
    print('gso_coefficients=', gso_coefficients)