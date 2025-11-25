import time
from time import time # или

# start = time()
# end = time()
# print(end - start)

from timeit import timeit

a = list(range(10_000_000))
b = set(a)
c = tuple(a)


print(format(a.__sizeof__(),","))
print(format(b.__sizeof__(),","))
print(format(c.__sizeof__(),","))



print(timeit("111 in a", globals={"a":a}, number=1_000_000))
print(timeit("111 in a", globals={"a":b}))
print(timeit("111 in a", globals={"a":c}))
