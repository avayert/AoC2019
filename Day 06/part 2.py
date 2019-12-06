from collections import defaultdict

graph = defaultdict(set)

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parent, child = line.strip().split(')')
        # add both so it's undirected
        graph[parent].add(child)
        graph[child].add(parent)

seen = set()
to_search = [(graph['YOU'], 0)]

while to_search:
    children, depth = to_search.pop()

    for node in children:
        if node == 'SAN':
            break

        if node in seen:
            continue

        if node not in graph:
            continue

        seen.add(node)
        to_search.append((graph[node], depth + 1))
    else:
        continue

    # we have found santa
    print(depth - 1)
    break
