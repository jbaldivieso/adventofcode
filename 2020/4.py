test_input = """
ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""

test2_input_valid = """
pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""

test2_input_invalid = """
eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""


def parse_input(data):
    """Return list of "passports" (dicts)."""
    # List of strings
    pps = data.split("\n\n")
    # List of lists of strings (split on any white space)
    pps = [pp.split() for pp in pps]
    # List of dicts (passports).
    results = []
    for pp in pps:
        result = {}
        for item in pp:
            k, v = item.split(":")
            result[k] = v
        results.append(result)
    return results


def p1(data):
    def is_valid(passport):
        required_fields = {
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
            }
        return required_fields.issubset(set(passport.keys()))

    passports = parse_input(data)
    valid = 0
    for passport in passports:
        if is_valid(passport):
            valid += 1
    return valid


def p2(data):
    def is_valid(passport):
        field = passport.get("byr", "")
        if not (field.isdecimal() and 1920 <= int(field) <= 2002):
            return False
        field = passport.get("iyr", "")
        if not (field.isdecimal() and 2010 <= int(field) <= 2020):
            return False
        field = passport.get("eyr", "")
        if not (field.isdecimal() and 2020 <= int(field) <= 2030):
            return False
        field = passport.get("hgt", "")
        if field[-2:] == "cm":
            if not (field[:-2].isdecimal() and 150 <= int(field[:-2]) <= 193):
                return False
        elif field[-2:] == "in":
            if not (field[:-2].isdecimal() and 59 <= int(field[:-2]) <= 76):
                return False
        else:
            return False
        field = passport.get("hcl", "")
        if not (len(field) == 7 and field[0] == "#"):
            return False
        try:
            int(field[1:], 16)
        except ValueError:
            return False
        field = passport.get("ecl")
        if field not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
            return False
        field = passport.get("pid", "")
        if not (len(field) == 9 and field.isdecimal()):
            return False
        return True

    passports = parse_input(data)
    valid = 0
    for passport in passports:
        if is_valid(passport):
            valid += 1
    return valid


if __name__ == "__main__":
    assert(p1(test_input) == 2)
    with open("4-input.txt") as f:
        data = f.read()
    print(p1(data))
    assert(p2(test2_input_valid) == 4)
    assert(p2(test2_input_invalid) == 0)
    print(p2(data))
