def turn(array, a, b, c, d):
    min_val = array[a][b]

    # now
    x, y = c, d

    edge1 = array[a + 1][b]
    edge2 = array[a][d]
    edge3 = array[c][d]
    edge4 = array[c][b]

    # →
    while y > b:
        array[a][y] = array[a][y - 1]
        min_val = min(min_val, array[a][y])
        y -= 1
    array[a][b] = edge1

    # ↓
    while x > a:
        array[x][d] = array[x - 1][d]
        min_val = min(min_val, array[x][d])
        x -= 1
    array[a + 1][d] = edge2

    # ←
    y = b
    while y < d:
        array[c][y] = array[c][y + 1]
        min_val = min(min_val, array[c][y])
        y += 1
    array[c][d - 1] = edge3

    # ↑
    while x < c:
        array[x][b] = array[x + 1][b]
        min_val = min(min_val, array[x][b])
        x += 1
    array[c - 1][b] = edge4

    return min(min_val, edge1, edge2, edge3, edge4)


def solution(rows, columns, queries):
    result = []

    array = []
    for r in range(1, rows + 1):
        array.append(list(range((r - 1) * columns + 1, r * columns + 1)))

    for q in queries:
        a, b, c, d = q
        a -= 1
        b -= 1
        c -= 1
        d -= 1
        result.append(turn(array, a, b, c, d))

    return result

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))