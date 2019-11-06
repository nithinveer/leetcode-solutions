def numSmallerByFrequency( queries, words):
    rtn_lst = []
    query_val = []
    for each_query in queries:
        query_val.append(each_query.count(min(each_query)))
    word_val = []
    for each_word in words:
        word_val.append(each_word.count(min(each_word)) )
    for each_query in query_val:
        cnt = 0
        for each_word in word_val:
            # print(each_query.count(min(each_query)), each_word.count(min(each_query)))
            if each_query < each_word:
                cnt+=1
        rtn_lst.append(cnt)
    return(rtn_lst)





if __name__ == '__main__':
    queries = ["bbb", "cc"]
    words = ["a", "aa", "aaa", "aaaa"]
    print(numSmallerByFrequency(queries,words))