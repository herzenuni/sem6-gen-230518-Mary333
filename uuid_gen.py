import itertools
import uuid

def create_uuid_gen():
    while True:
        yield uuid.uuid4()

uuid_gen = create_uuid_gen()

print(next(uuid_gen))
print(next(uuid_gen))
print(next(uuid_gen))