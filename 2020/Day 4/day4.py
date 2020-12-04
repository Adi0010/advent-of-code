import re
f = open('input.txt')
a = f.read().strip().split("\n\n")
passports = []
for entry in a:
    passport = {}
    for e in entry.replace("\n", " ").split(" "):
        k, v = e.split(":")
        passport[k] = v
    passports.append(passport)

count1 = 0
count2 = 0




def check_byr(s):
    return 1920 <= int(s) <= 2002


def check_iyr(s):
    return 2010 <= int(s) <= 2020


def check_eyr(s):
    return 2020 <= int(s) <= 2030


def check_height(s):
    match = re.match(r'^([0-9]+)(cm|in)$', s)
    if match:
        g = match.groups()
        return (g[1] == "cm" and 150 <= int(g[0]) <= 193) or (g[1] == "in" and 59 <= int(g[0]) <= 76)


def check_hcl(s):
    return re.match(r'^#[0-9a-f]{6}$', s)


def check_pid(s):
    return re.match(r'^[0-9]{9}$', s)


def check_ecl(s):
    return s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

for value in passports:
    if all(key in value for key in ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")):
        count1+=1
        if check_byr(value["byr"]):
            if check_iyr(value["iyr"]):
                if check_eyr(value["eyr"]):
                    if check_height(value["hgt"]):
                        if check_hcl(value["hcl"]):
                            if check_ecl(value["ecl"]):
                                if check_pid(value["pid"]):
                                    count2 += 1

print(count1,count2)
