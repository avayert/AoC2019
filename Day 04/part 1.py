with open('input.txt', 'r', encoding='utf-8') as file:
    low, high = [int(number) for number in file.read().split('-')]


def predicate(number):
    number = str(number)

    if not any(a == b for a, b in zip(number, number[1:])):
        return False

    return all(a <= b for a, b in zip(number, number[1:]))


print(sum(predicate(number) for number in range(low, high)))
