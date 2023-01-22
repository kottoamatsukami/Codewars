def snail(snail_map: list) -> list:
    out = []
    while len(snail_map) != 0:
        out += snail_map[0]
        snail_map.pop(0)
        if len(snail_map) == 0: break
        for i, x in enumerate(snail_map):
            out += [x[-1]]
            snail_map[i] = snail_map[i][:-1]
        if len(snail_map) == 0: break
        out += snail_map[-1][::-1]
        snail_map.pop(-1)
        if len(snail_map) == 0: break
        for i, x in enumerate(snail_map[::-1]):
            out += [x[0]]
            snail_map[i] = snail_map[i][1:]
        if len(snail_map) == 0: break
    return out