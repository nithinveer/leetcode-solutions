import sys
def greedy_coins(weight, denominations):
    denominations_map = {}
    denominations.sort(reverse = True)
    for each_deomination in denominations:
        while weight >= each_deomination:
            if each_deomination not in denominations_map:
                denominations_map[each_deomination] =0
            denominations_map[each_deomination] +=1
            weight  -= each_deomination

    return denominations_map


def minCoins(weight, denominations):
    table = [0 for i in range(weight + 1)]
    # print(table)
    table[0] = 0
    for i in range(1, weight + 1):
        table[i] = sys.maxsize
    print(table)
    for i in range(1, weight + 1):
        for j in range(len(denominations)):
            if (denominations[j] <= i):
                temp_result = table[i - denominations[j]]
                if (temp_result != sys.maxsize and temp_result + 1 < table[i]):
                    table[i] = temp_result + 1
    print(table)
    return table[weight]

def dp_coins(weight,denominations):
    matrix = [[0 for i in range(weight+1)] for j in range(len(denominations))]
    for i in range(1, weight+1):
        if denominations[0] == 1:
            matrix[0][i] = i
        else:
            if i % (denominations[0]) == 0:
                matrix[0][i] = 0
            else:
                matrix[0][i] = 1
    for i in range(1, len(denominations)):
        for j in range(1, weight+1):
            if denominations[i] > j:
                matrix[i][j] = matrix[i-1][j]
            else:
                matrix[i][j] = min(matrix[i-1][j], 1+matrix[i][j-denominations[i]])
    total_no_ofways=matrix[len(denominations)-1][weight]
    denominations_map = {}
    row_count = len(denominations) - 1
    while weight > 0 and row_count > 0:
        if matrix[row_count][weight] == matrix[row_count - 1][weight]:
            row_count -= 1
        else:
            if denominations[row_count] not in denominations_map:
                denominations_map[denominations[row_count]] = 1
            else:
                denominations_map[denominations[row_count]] += 1
            weight = weight - denominations[row_count]
    else:
        if row_count == 0 and weight > 0:
            while weight > 0:
                if denominations[row_count] not in denominations_map:
                    denominations_map[denominations[row_count]] = 1
                else:
                    denominations_map[denominations[row_count]] += 1
                weight = weight - 1
    # print(denominations_map)
    return total_no_ofways, denominations_map


if __name__ == '__main__':
    deno = [1,5,10,25,50,100]
    we = 1728
    print(dp_coins(we, deno))