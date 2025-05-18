def inner_product(l1, l2):
    return sum(x*y for x,y in zip(l1, l2))

def norm(l):
    return pow(sum(x**2 for x in l), 0.5)

def mult_list(l, x):
    return [x*y for y in l]

def add_list(l1, l2):
    return [x+y for x,y in zip(l1, l2)]

def lagrange_basis_reduction(ordered_basis):
    # ラグランジュ基底簡約は2次元格子に対するアルゴリズムであるため、2次元格子以外を受け付けない
    if len(ordered_basis)!=2:
        return ordered_basis, False

    b1 = ordered_basis[0]
    b2 = ordered_basis[1]

    if norm(b1) > norm(b2):
        b1, b2 = b2, b1
    
    # Pythonにdo while文は無いので代用
    while True:
        q = - round(inner_product(b1, b2)/(norm(b1)**2))
        v = add_list(b2, mult_list(b1, q))
        b2, b1 = b1, v
        
        print(q)
        print(v)

        if norm(b1) >= norm(b2):
            break

    b1, b2 = b2, b1

    return [b1, b2], True


if __name__ == '__main__':
    # 参考文献の例にある格子基底でテスト
    test_ordered_basis = [[-7, -4, -10], [9, 5, 12]]
    #test_ordered_basis = [[230, -651, 609, -366], [301, -852, 797, -479]]

    lagrange_reduced_basis, is_reduced = lagrange_basis_reduction(test_ordered_basis)

    print('lagrange_reduced_basis=', lagrange_reduced_basis)
    print('is_reduced=', is_reduced)