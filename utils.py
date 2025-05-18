def inner_product(l1, l2):
    return sum(x*y for x,y in zip(l1, l2))

def norm(l):
    return pow(sum(x**2 for x in l), 0.5)

def mult_list(l, x):
    return [x*y for y in l]

def add_list(l1, l2):
    return [x+y for x,y in zip(l1, l2)]