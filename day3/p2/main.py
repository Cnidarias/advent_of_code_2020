def main():
    with open("../input.txt", 'r') as f:
        map = [r.strip() for r in f.readlines()]
        trees, spaces = get_trees_and_spaces(map, 1, 1)
        trees2, spaces2 = get_trees_and_spaces(map, 3, 1)
        trees3, spaces3 = get_trees_and_spaces(map, 5, 1)
        trees4, spaces4 = get_trees_and_spaces(map, 7, 1)
        trees5, spaces5 = get_trees_and_spaces(map, 1, 2)

        print(trees * trees2 * trees3 * trees4 * trees5)


def get_trees_and_spaces(map, r, d):
    max_width = len(map[0])
    current_d = 0
    current_r = 0

    space_counter = 0
    tree_counter = 0
    while current_d < len(map):
        if map[current_d][current_r % max_width] == '.':
            space_counter += 1
        else:
            tree_counter += 1
        current_d += d
        current_r += r
    return tree_counter, space_counter


if __name__ == "__main__":
    main()
