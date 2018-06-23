import itertools
import uuid

def fib():
  first = 0
  second = 1
  
  while True:
    yield first
    second = first + second
    yield second
    first = first + second

fib_gen = fib()
print(list(itertools.islice(fib_gen, 10)))