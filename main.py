MAX_SIZE = 9
START_POINTS = 10
STRING = 3
COLUMN = 3


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

marks = list(items.keys())

def live_points_sign_check(items, points):
    all_live_points = 0
    for i, (_,value) in enumerate(items.items()):
        all_live_points += value['live_points']
    points += START_POINTS
    if all_live_points - points < points:
        return points - (all_live_points - points)
    else:
        return False


def gen_tab(items, max_size=MAX_SIZE):
    table = [[0 for c in range(max_size)] for _ in range(len(items))]
    for i, (_, value) in enumerate(items.items()):
        size = value['size']
        live_points = value['live_points']

        for limit_size in range(1, max_size + 1):
            col = limit_size - 1
            if i == 0:
                if size > limit_size:
                    table[i][col] = 0  
                else:
                    table[i][col] = live_points
            else:
                pre_live_points = table[i-1][col]
                if size > limit_size:
                    table[i][col] = pre_live_points
                else:
                    if col < size:
                        used = 0 
                    else:
                        used = table[i-1][col - size]

                    new_live_points = used + live_points

                    res = max(new_live_points, pre_live_points)
                    table[i][col] = res
    
    return table


def gen_inventory(marks, item_size_list, complect):
    key_value_list = []
    for i in range(len(marks)):
        if marks[i] in complect:
            key_value_list.append((marks[i], item_size_list[i]))

    key_value_list = sorted(key_value_list, key=lambda x: x[1], reverse=True)
    table = [[0 for _ in range(STRING)] for _ in range(COLUMN)]
    s = 0 #strings
    for i in range(len(key_value_list)):
        c = 0 #columns
        count = key_value_list[i][1]
        while count > 0:
            if table[s][c] == 0:
                table[s][c] = key_value_list[i][0]
                count -= 1
                c += 1
            else:
                c += 1
        if s + 1 < STRING:
            s += 1
        else:
            s = 0

    for i in range(len(table)):
        print(table[i])


def item_complect(table, items):
    item_size = []
    for i, (_, value) in enumerate(items.items()):
            size = value['size']
            item_size.append(size)

    avaibale_size = MAX_SIZE - 1
    complect = []
    for k in range(len(table) - 1, -1, -1):
        if avaibale_size - item_size[k] > -2:
            if table[k][avaibale_size] != table[k - 1][avaibale_size]:
                complect.append(marks[k])
                avaibale_size = avaibale_size - item_size[k]

    
    final_points = live_points_sign_check(items, table[len(table) - 1][MAX_SIZE - 1])
    
    if final_points > 0:
        gen_inventory(marks, item_size, complect)
        print(f'Итоговый счёт выживания: {final_points}')
    else:
        return 'Error'


if __name__ == '__main__':
    table = gen_tab(items)
    item_complect(table, items)
