import string


def read_field(filename):
    with open(filename, "r", encoding="utf-8", errors="ignore") as f:
        field = [[0] * 10 for i in range(10)]
        data = f.readlines()
        for i in range(10):
            for j in range(len(data[i][:10])):
                if data[i][j] == "*":
                    field[i][j] = 1
                elif data[i][j] == "X":
                    field[i][j] = "X"
    return field


def has_ship(field, coords):
    lets = list(string.ascii_uppercase[:10])
    if field[coords[1] - 1][lets.index(coords[0])] == 1:
        return True
    return False


def ship_size(field, coords):
    lets = list(string.ascii_uppercase[:10])
    pass






a = read_field("field.txt")

for i in a:
    print(i)

print(has_ship(a, ("D", 1)))
