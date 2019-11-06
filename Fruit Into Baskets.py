def totalFruitold1( tree):
    max_ln = 2
    temp_set = set()
    temp_count = 0
    index = 0
    las_ele = tree[0]
    las_index = 0
    while index < len(tree):
        # print(index)
        if tree[index] in temp_set:
            temp_count +=1
            if las_ele != tree[index]:
                las_ele = tree[index]
                las_index = index
            index+=1
        else:
            length = len(temp_set)
            if length == 0:
                temp_set.add(tree[index])
                temp_count +=1
                las_ele = tree[index]
                las_index = index
                index+=1
            elif length ==1:
                temp_set.add(tree[index])
                temp_count+=1
                las_ele = tree[index]
                las_index = index
                index +=1
            elif length == 2:
                if temp_count >max_ln:
                    max_ln = temp_count
                temp_set = set()
                temp_count = 0
                index = las_index

    # if temp_count > max_ln:
    #     max_ln = temp_count
    return  max(max_ln,temp_count)



if __name__ == '__main__':
    tree = [1,2,1]
    print(totalFruitold1(tree))