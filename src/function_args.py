def product(*args):
    product = 1
    for num in args:
        product = product * num
    return product

product = product(1,2,3,4)
print(product)

