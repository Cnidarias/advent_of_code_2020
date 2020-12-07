def main():
    with open("../input.txt", 'r') as f:
        map = [r.strip() for r in f.readlines()]
        max_width = len(map[0])
        r = 3
        d = 1

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

        print(space_counter, tree_counter)


if __name__ == "__main__":
    main()
