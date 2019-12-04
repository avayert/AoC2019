from collections import Counter

with open('input.txt', 'r', encoding='utf-8') as file:
    low, high = [int(number) for number in file.read().split('-')]


def predicate(number):
    number = str(number)

    if not all(a <= b for a, b in zip(number, number[1:])):
        return False

    occurences = Counter(number)
    return any(times == 2 for times in occurences.values())


print(sum(predicate(number) for number in range(low, high)))
