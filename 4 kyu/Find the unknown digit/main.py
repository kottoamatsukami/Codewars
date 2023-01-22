import re


def solve_runes(runes):
    pattern = r"(-*[\d?]+)(\+|\-|\*)(-*[\d?]+)=(-?[\d?]+)"
    out = -1
    for d in range(10)[::-1]:
        res = re.findall(pattern, runes.replace("?", str(d)))[0]
        if not (str(int(res[0])) == res[0] and str(int(res[2])) == res[2] and str(int(res[3])) == res[3]): continue
        if str(d) in runes: continue

        if res[1] == "+":
            if int(res[0]) + int(res[2]) == int(res[3]):
                out = d
        elif res[1] == "-":
            if int(res[0]) - int(res[2]) == int(res[3]):
                out = d
        elif res[1] == "*":
            if int(res[0]) * int(res[2]) == int(res[3]):
                out = d
    return out