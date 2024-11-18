MAX_SIZE = 9

items = {
    'r': {'size': 3, 'live_points':25},
    'p': {'size': 2, 'live_points':15},
    'a': {'size': 2, 'live_points':15},
    'm': {'size': 2, 'live_points':20},
    'i': {'size': 1, 'live_points':5},
    'k': {'size': 1, 'live_points':15},
    'x': {'size': 3, 'live_points':20},
    't': {'size': 1, 'live_points':25},
    'f': {'size': 1, 'live_points':15},
    'd': {'size': 1, 'live_points':10},
    's': {'size': 2, 'live_points':20},
    'c': {'size': 2, 'live_points':20},
}

def gen_tab(items, max_size=MAX_SIZE):
    table = [[0 for c in range(max_size)] for _ in range(len(items))]
    for i, (_, value) in enumerate(items.items()):
        size = value['size']
        live_points = value['live_points']

        for limit_size in range(1, max_size + 1):
            col = limit_size - 1
            if i == 0:
                table[i][col] = 0 if size > limit_size else live_points
            else:
                pre_live_points = table[i-1][col]
                if size > limit_size:
                    table[i][col] = pre_live_points
                else:
                    used = 0 if col < size else table[i-1][col - size]
                    new_live_points = used + live_points

                    res = max(new_live_points, pre_live_points)
                    table[i][col] = res
    
    return table

if __name__ == '__main__':
    table = gen_tab(items)
    for i in range(len(table)):
        print(i + 1, table[i])