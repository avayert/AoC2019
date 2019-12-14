import collections
from dataclasses import dataclass
from math import ceil
from typing import List


@dataclass
class Reactant:
    name: str
    amount: int


@dataclass
class Reaction:
    reactants: List[Reactant]
    product: Reactant


reactions = []

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        required, product = line.split('=>')
        required = required.split(',')

        amount, name = product.strip().split()
        product = Reactant(name, int(amount))
        reaction = Reaction([], product)

        for item in required:
            amount, name = item.strip().split()
            reaction.reactants.append(Reactant(name, int(amount)))

        reactions.append(reaction)


def get_ore(fuel: int):
    needed = collections.defaultdict(int, FUEL=fuel)
    leftover = collections.defaultdict(int)
    ore_used = 0

    while needed:
        item, amount = needed.popitem()

        if item == 'ORE':
            ore_used += amount

            if ore_used > 10 ** 12:
                return 10 ** 12 + 1

            continue

        left = min(leftover[item], amount)
        need = amount - left
        leftover[item] -= left

        reaction = next(reaction for reaction in reactions if reaction.product.name == item)

        created = ceil(need / reaction.product.amount)

        leftover[item] += created * reaction.product.amount - need

        for reactant in reaction.reactants:
            needed[reactant.name] += reactant.amount * created

    return ore_used


# the result for part 1 was ~100k so I can ballpark these bounds
low = 500_000
high = 10_000_000

while (high - low) > 1:
    print(low, high)
    middle = (high + low) // 2
    ore_required = get_ore(middle)

    if ore_required > 10 ** 12:
        high = middle
    else:
        low = middle

print(low)
