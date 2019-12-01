with open('input.txt', 'r', encoding='utf-8') as file:
    print(sum(int(line) // 3 - 2 for line in file))
