def decorator_function(func):
    print("estou na primeira")

    def closure_function(*args):
        print("Estou na segunda")
        return func(*args)

    return closure_function


@decorator_function
def soma(x, y):
    print(x + y)


resultado = soma(1, 1)
print(soma.__name__)
