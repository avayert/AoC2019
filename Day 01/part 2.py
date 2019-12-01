total = 0

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        module_mass = int(line)

        while True:
            fuel = module_mass // 3 - 2

            if fuel <= 0:
                break

            total += fuel
            module_mass = fuel

print(total)
