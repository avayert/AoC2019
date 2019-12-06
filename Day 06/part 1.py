from collections import defaultdict

graph = defaultdict(list)

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parent, child = line.strip().split(')')
        graph[parent].append(child)


# I sure hope I don't run into the recursion limit
def traverse(node, depth=0):
    if node not in graph:
        return depth

    return depth + sum(traverse(child, depth + 1) for child in graph[node])


print(traverse('COM'))
