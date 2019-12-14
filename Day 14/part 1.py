import collections
from dataclasses import dataclass
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

needed = collections.defaultdict(int, FUEL=1)
leftover = collections.defaultdict(int)
ore_used = 0

while needed:
    item, amount = needed.popitem()

    if item == 'ORE':
        ore_used += amount
        continue

    left = min(leftover[item], amount)
    need = amount - left
    leftover[item] -= left

    reaction = next(reaction for reaction in reactions if reaction.product.name == item)

    while need > 0:
        need -= reaction.product.amount
        for reactant in reaction.reactants:
            needed[reactant.name] += reactant.amount

        if need < 0:
            leftover[item] += abs(need)

print(ore_used)
