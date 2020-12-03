def count_trees(forest, steps):
    pos = (0, 0)
    numTrees= 0

    while pos[1] < len(forest):
        if forest[pos[1]][pos[0] % len(forest[0])] == '#':
            numTrees += 1

        pos = (pos[0] + steps[0], pos[1] + steps[1])

    return numTrees

with open("input.txt") as f:
    forest = []
    for row in f:
        forest.append(row.strip())


    print("Count of Trees", count_trees(forest, (3, 1)))

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for step in slopes:
        product *= count_trees(forest, step)

    print("Product ", product)