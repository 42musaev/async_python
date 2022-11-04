from time import time


def generator_name(name: str) -> str:
    for letter in name:
        yield letter


def generator_number(number: int) -> int:
    for number in range(number):
        yield number


g1 = generator_name('name')
g2 = generator_number(10)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
