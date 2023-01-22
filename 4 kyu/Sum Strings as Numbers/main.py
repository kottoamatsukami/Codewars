def sum_strings(x: str, y: str):
    new_x = x.replace("-", "")
    new_y = y.replace("-", "")
    lx, ly = len(new_x), len(new_y)
    if lx == 0: return y if y != "" else '0'
    elif ly == 0: return x if x != "" else '0'
    first, second = (new_x[::-1], new_y.zfill(lx)[::-1]) if lx > ly else (new_y[::-1], new_x.zfill(ly)[::-1])
    f_sign = "-" if x[0] == "-" else "+"
    s_sign = "-" if y[0] == "-" else "+"
    if f_sign == s_sign:
        ost = 0
        out = ""
        for i in range(max(lx, ly)):
            n = int(first[i]) + int(second[i]) + ost
            ost = n//10
            out += str(n % 10)
        out += str(ost)
        res = ""
        for char in out[::-1]:
            if char != "0" or len(res) > 0:
                res += char
        return "-" + res if f_sign == "-" else (res if res != "" else "0")
    else:
        ost = 0
        out = ""
        for i in range(max(lx, ly)):
            n = int(first[i]) - int(second[i]) + ost
            ost = n // 10
            out += str(n[-1]) if n > 0 else str(10+n)[-1]
        out += str(ost)
        res = ""
        for char in out[::-1]:
            if char != "0" or len(res) > 0:
                res += char
        if lx > ly and x[0] == "-" or lx < ly and y[0] == "-":
            return "-"+res
        return res if res != "" else "0"