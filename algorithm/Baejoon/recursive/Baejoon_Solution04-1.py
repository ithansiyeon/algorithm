import sys

n = int(sys.stdin.readline().rstrip())

def star_print(size):
    stars = []
    result = []
    if size == 1:
        stars.append('*')
        return stars
    else:
        size = size // 3
    stars = star_print(size)

    for s in stars:
        result.append(s*3)
    for s in stars:
        result.append(s+" "*size+s)
    for s in stars:
        result.append(s*3)

    return result
answer = star_print(n)
print("\n".join(answer))
