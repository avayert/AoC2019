import subprocess
from concurrent.futures.thread import ThreadPoolExecutor
from itertools import permutations

with open('input.txt', 'r', encoding='utf-8') as file:
    tape = file.read().strip()


def run_computer(permutation):
    previous = 0

    for digit in permutation:
        process = subprocess.run(f'python computer.py {tape}', input=f'{digit}\n{previous}\n'.encode(),
                                 stdout=subprocess.PIPE)
        previous = int(process.stdout)

    return previous


with ThreadPoolExecutor() as pool:
    futures = []

    for permutation in permutations(range(5)):
        futures.append(pool.submit(run_computer, permutation))

    print(max(future.result() for future in futures))
