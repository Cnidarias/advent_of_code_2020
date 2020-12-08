def main():
    with open("../input.txt", "r") as f:
        seat_ids = sorted([get_seat_id(get_row(l.strip()[0:7]), get_col(l.strip()[7:])) for l in f.readlines()])
    for i in range(1, len(seat_ids) - 1, 1):
        n = seat_ids[i]
        if seat_ids[i - 1] != n - 1:
            print(n - 1)


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
