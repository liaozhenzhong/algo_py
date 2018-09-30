def abstract_string(strA, strB):
    lenA = len(strA) + 1
    lenB = len(strB) + 1

    match = [[0] * lenB for _ in range(lenA)]
    source = [[''] * lenB for _ in range(lenA)]

    for y in range(1, lenA):
        for x in range(1, lenB):
            match[y][x] = max(match[y-1][x], match[y][x-1])
            source[y][x] = 'left' if match[y][x-1] >= match[y-1][x] else 'top'
            if strA[y-1] == strB[x-1]:
                match[y][x] += 1

    return match, source

def path_backward(strA, match, source, y, x):
    if match[y][x] ==  1 + max(match[y-1][x], match[y][x-1]):
        yield strA[y-1]

    if y == 0 or x == 0:
        return
    elif source[y][x] == 'left':
        yield from path_backward(strA, match, source, y, x-1)
    else:
        yield from path_backward(strA, match, source, y-1, x)

