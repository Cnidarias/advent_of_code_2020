def main():
    valids = 0
    with open("../input.txt", 'r') as f:
        for l in f.readlines():
            minmax, letter, pw = l.split(" ")
            min_val, max_val = minmax.split("-")
            min_val, max_val = int(min_val), int(max_val)
            letter = letter.rstrip(":")

            if check_pw(min_val, max_val, letter, pw):
                valids += 1
    print(valids)


def check_pw(min_count: int, max_count: int, letter: str, pw: str) -> bool:
    return min_count <= pw.count(letter) <= max_count


if __name__ == '__main__':
    main()
