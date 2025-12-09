
"""
Написать генератор factorial, который возвращает подряд значения факториала

Например:

factorial_gen = factorial()

next(factorial_gen) -> 1
next(factorial_gen) -> 2
next(factorial_gen) -> 6
next(factorial_gen) -> 24
"""
def factorial():
    n = 2
    fact = 1

    while True:
        yield fact
        fact = fact * n
        n += 1

gen = factorial()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))