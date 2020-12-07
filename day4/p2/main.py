import itertools
# 181 is too low
def main():
    all_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_count = 0
    with open("../input.txt", "r") as f:
        everything = f.read()
        passports = everything.split("\n\n")

        for passport in passports:
            if verify_passport_has_fields(passport, required_fields):
                valid_count += 1
    print(valid_count)

def verify_passport_has_fields(passport, required_fields):
    parts =passport.split("\n")
    all_parts = [p.split(" ") for p in parts if len(p) > 1]
    flat_list= list(itertools.chain(*all_parts))
    fields = [r.split(":")[0] for r in flat_list]
    values: [str] = [r.split(":")[1] for r in flat_list]
    print("---")
    print(passport)
    print(flat_list)
    print(fields, values)
    print("---")

    for rf in required_fields:
        if rf not in fields:
            return False

    # bad code
    for field, value in zip(fields, values):
        if field == 'byr' and not (value.isnumeric() and int(value) >= 1920 and int(value) <= 2002):
            return False
        elif field == 'iyr' and not (value.isnumeric() and int(value) >= 2010 and int(value) <= 2020):
            return False
        elif field == 'eyr' and not (value.isnumeric() and int(value) >= 2020 and int(value) <= 2030):
            return False
        elif field == 'hgt':
            if value.endswith("cm"):
                n = value.rstrip("cm")
                if not n.isnumeric():
                    return False
                if int(n) < 150 or int(n) > 193:
                    return False
            elif value.endswith("in"):
                n = value.rstrip("in")
                if not n.isnumeric():
                    return False
                if int(n) < 59 or int(n) > 76:
                    return False
            else:
                return False
        elif field == 'hcl' and not (len(value) == 7 and value[0] == "#" and value[1:].isalnum()):
            return False
        elif field == 'ecl' and value not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return False
        elif field == 'pid' and not (len(value) == 9 and value.isnumeric()):
            return False

    return True



if __name__ == "__main__":
    main()
