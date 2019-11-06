def findRestaurant( list1, list2):
    rtn = 2000
    rtn_list = []
    if len(list1) < len(list2):
        for each_el in list1:
            if each_el in list2:
                if (list1.index(each_el) + list2.index(each_el)) == rtn:
                    rtn_list.append(each_el)
                elif  (list1.index(each_el) + list2.index(each_el)) < rtn:
                    rtn = (list1.index(each_el) + list2.index(each_el))
                    rtn_list = []
                    rtn_list.append(each_el)

    else :
        for each_el in list2:
            if each_el in list1:
                if (list1.index(each_el) + list2.index(each_el)) == rtn:
                    rtn_list.append(each_el)
                elif (list1.index(each_el) + list2.index(each_el)) < rtn:
                    rtn = (list1.index(each_el) + list2.index(each_el))
                    rtn_list = []
                    rtn_list.append(each_el)

    return rtn_list





if __name__ == '__main__':
    list1 = ["KFC", "Tapioca Express", "Burger King", "Shogun"]
    list2 = ["Shogun", "KFC", "Burger King"]
    print(findRestaurant(list1,list2))