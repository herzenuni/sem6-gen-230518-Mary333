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

def create_uuid_gen():
    return (uuid.uuid4() for _ in itertools.count())

print(next(gen_exp))
print(next(gen_exp))

fib_gen = fib()
print(list(itertools.islice(fib_gen, 10)))