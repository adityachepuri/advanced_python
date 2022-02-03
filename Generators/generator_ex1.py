def mygen():
    yield 'A'
    yield 'B'
    yield 'C'
    yield 'D'

g=mygen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
