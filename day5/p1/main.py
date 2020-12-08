def main():
    max_seat_id = -1
    with open("../input.txt", "r") as f:
        for l in f.readlines():
            l = l.strip()
            row = get_row(l[0:7])
            col = get_col(l[7:])
            max_seat_id = max(max_seat_id, get_seat_id(row, col))
    print(max_seat_id)


def get_seat_id(row: int, col: int) -> int:
    return row * 8 + col


def get_row(chars: str, start: int = 0, end: int = 127) -> int:
    return get_bounds(chars, start, end)


def get_col(chars: str, start: int = 0, end: int = 7) -> int:
    return get_bounds(chars, start, end)


def get_bounds(chars: str, min_num: int, max_num: int) -> int:
    if min_num == max_num:
        return min_num
    half = chars[0]
    if half == "F" or half == "L":
        return get_bounds(chars[1:], min_num, max_num - ((max_num - min_num) // 2 + 1))
    else:
        return get_bounds(chars[1:], min_num + ((max_num - min_num) // 2 + 1), max_num)


if __name__ == "__main__":
    main()
