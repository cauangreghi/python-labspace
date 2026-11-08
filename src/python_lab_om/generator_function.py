def list_of_clubs():
    print("Primeiro clube")
    yield 1
    print("segundo clube")
    yield
    print("terceiro clube")


teste = list_of_clubs()
try:
    next(teste)
    next(teste)
    next(teste)
except StopIteration as ex:
    print("Lista finalizada")
