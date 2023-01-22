def move_zeros(lst: list) -> list:
    return [x for x in lst if x != 0] + [0]*lst.count(0)
