def read_input():
    f = open("input.txt", "r")
    risk_field = []
    for line in f.readlines():
        char_field = []
        for char in line.strip():
            char_field.append(int(char))
        risk_field.append(char_field)
    return risk_field


def getMinCostField(cost):
    min_field = [[0 for x in range(len(cost))] for x in range(len(cost[0]))]

    for i in range(1, len(cost)):
        min_field[i][0] = min_field[i - 1][0] + cost[i][0]

    for j in range(1, len(cost[0])):
        min_field[0][j] = min_field[0][j - 1] + cost[0][j]

    for i in range(1, len(cost)):
        for j in range(1, len(cost[0])):
            min_field[i][j] = min(min_field[i - 1][j], min_field[i][j - 1]) + cost[i][j]
    return min_field


def find_shortest_path(is_big=False):
    field = read_input()
    return getMinCostField(field)[len(field) - 1][len(field[0]) - 1]


def print_array(array):
    for line in array:
        for value in line:
            print(value, end="")
        print()
    print()


if __name__ == "__main__":
    print(find_shortest_path())
