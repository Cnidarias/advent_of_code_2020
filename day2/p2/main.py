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

def check_pw(l_pos, r_pos, letter, pw):
    l_pos_has_char = pw[l_pos - 1] == letter
    r_pos_has_char = pw[r_pos - 1] == letter

    return True if l_pos_has_char != r_pos_has_char else False

if __name__ == '__main__':
    main()
