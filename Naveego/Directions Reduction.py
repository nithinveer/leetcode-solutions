def dirReduc(arr):
    dir_map = {
        'north': 'south',
        'east': 'west',
        'west': 'east',
        'south': 'north'
    }
    rtn_lst = []
    for ech_dir in arr:
        if len(rtn_lst) == 0:
            rtn_lst.append(ech_dir)
        else:
            if dir_map[ech_dir.lower()] == rtn_lst[-1].lower():
                rtn_lst.pop()
            else:
                rtn_lst.append(ech_dir)
        print(rtn_lst)
    return rtn_lst




if __name__ == '__main__':
    arr = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
    print(dirReduc(arr))