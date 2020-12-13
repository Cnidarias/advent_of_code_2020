def main():
    with open("../input.txt", "r") as f:
        sample_data = [
            "L.LL.LL.LL",
            "LLLLLLL.LL",
            "L.L.L..L..",
            "LLLL.LL.LL",
            "L.LL.LL.LL",
            "L.LLLLL.LL",
            "..L.L.....",
            "LLLLLLLLLL",
            "L.LLLLLL.L",
            "L.LLLLL.LL",
        ]
        sample_data = ['#.##.##.##', '#######.##', 'L.L.L..L..', '####.##.##', '#.##.##.##', '#.#####.##', '..#.#.....',
                       '##########',
                       '#.######.#', '#.#####.##']

        layout = [l.strip() for l in sample_data]
        layout = [l.strip() for l in f.readlines()]

        layout2 = generate_new_layout(layout)
        print(layout)
        print(layout2)
        while not are_layouts_equal(layout, layout2):
            layout = layout2
            layout2 = generate_new_layout(layout2)
            print(layout2)

        total_occupied_seats = sum([s.count("#") for s in layout])
        print(total_occupied_seats)


def are_layouts_equal(layout1, layout2):
    return all([x == layout2[idx] for idx, x in enumerate(layout1)])


def get_occupied_seats(row, col, layout_in):
    count = 0
    for r in range(3):
        for c in range(3):
            rc = row - 1 + r
            cc = col - 1 + c
            if 0 <= rc < len(layout_in) and 0 <= cc < len(layout_in[0]):
                if rc == row and cc == col:
                    continue
                if layout_in[rc][cc] == "#":
                    count += 1
    return count


def generate_new_layout(layout_in):
    layout = []

    for row, row_element in enumerate(layout_in):
        new_row = ""
        for col, col_element in enumerate(row_element):
            surrounding_occupied_seats = get_occupied_seats(row, col, layout_in)
            new_place = col_element
            if col_element == 'L' and surrounding_occupied_seats == 0:
                new_place = "#"
            if col_element == '#' and surrounding_occupied_seats >= 4:
                new_place = 'L'
            new_row += new_place
        layout.append(new_row)
    return layout


if __name__ == "__main__":
    main()
