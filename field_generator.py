import string


def read_field(filename):
    with open(filename, "r", encoding="utf-8", errors="ignore") as file_ships:
        field = [[0] * 10 for i in range(10)]
        data = file_ships.readlines()
        for i in range(10):
            for j in range(len(data[i][:10])):
                if data[i][j] == "*":
                    field[i][j] = 1
                elif data[i][j] == "X":
                    field[i][j] = "X"
    return field


def has_ship(field, coords):
    lets = list(string.ascii_uppercase[:10])
    if field[coords[1] - 1][lets.index(coords[0].upper())] == 1:
        return True
    return False


def ship_size(field, coords):
    lets = list(string.ascii_uppercase[:10])

    if not has_ship(field, coords):
        return (0, 0)

    ver, hor = coords[1] - 1, lets.index(coords[0].upper())
    horizontal, vertical = 1, 1

    step = 1
    while ver - step > 0 and field[ver - step][hor] == 1:
        vertical, step = vertical + 1, step + 1

    step = 1
    while ver + step < 10 and field[ver + step][hor] == 1:
        vertical, step = vertical + 1, step + 1

    step = 1
    while hor - step > 0 and field[ver][hor - step] == 1:
        horizontal, step = horizontal + 1, step + 1

    step = 1
    while hor + step < 10 and field[ver][hor + step] == 1:
        horizontal, step = horizontal + 1, step + 1

    return (horizontal, vertical)
