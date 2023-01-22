def dirReduc(arr: list) -> list:
    s = " ".join(arr)
    for i in range(len(arr)):
        s = s.replace("NORTH SOUTH", "")
        s = s.replace("SOUTH NORTH", "")
        s = s.replace("EAST WEST", "")
        s = s.replace("WEST EAST", "")
        s = s.replace("  ", " ")
    return s.split()
