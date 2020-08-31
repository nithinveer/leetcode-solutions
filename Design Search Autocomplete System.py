from collections import  defaultdict
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.dic = defaultdict(int)
        self.timex = defaultdict(list)
        tmex = 0
        for i in range(len(sentences)):
            self.dic[sentences[i]] = times[i]
            self.timex[times[i]].append(sentences[i])
            tmex = max(tmex, times[i])
        self.prefix = ""
        # self.matched = list(zip(self.dic.keys(), self.dic.values()))
        # print(self.matched)
        # s_matched = sorted(self.matched, key=lambda x: [-x[1], x[0]])
        # print(self.timex)
        for each in self.timex:
            tmp = self.timex[each]
            tmp.sort()
            self.timex[each] = tmp[:3]
        # print(self.timex)
        self.rtns =defaultdict(list)
        for t in range(tmex, -1, -1):
            for each in self.timex[t]:
                tmp =''
                for char in each:
                    tmp+=char
                    # if len(self.rtns[tmp]) < 3:
                    self.rtns[tmp].append(each)
        # print(self.rtns)





        # rtns = defaultdict(list)
        # sents = defaultdict(list)
        # tmex = 0
        # for i in range(len(sentences)):
        #     sents[times[i]].append(sentences[i])
        #     tmex = max(tmex, times[i])
        # # print(tmex)
        # for t in range(tmex, -1, -1):
        #     for each in sents[t]:
        #         tmp =''
        #         for char in each:
        #             tmp+=char
        #             if len(rtns[tmp]) < 3:
        #                 rtns[tmp].append(each)
        # print(rtns)






    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == "#":
            self.dic[self.prefix] += 1
            self.timex[self.dic[self.prefix]].append(self.prefix)
            tmp =  self.timex[self.dic[self.prefix]]
            tmp.sort()
            self.timex[self.dic[self.prefix]] = tmp[:3]
            tmp = ''
            for char in self.prefix:
                tmp += char
                self.rtns[tmp].append(self.prefix)


            # self.matched = list(zip(self.dic.keys(), self.dic.values()))
            self.prefix = ""
            # print(self.dic)
            return []
        else:
            self.prefix = self.prefix + c
            return self.rtns[self.prefix][:3]




ac = AutocompleteSystem(["i love you","island","iroman","i love leetcode"],[5,3,2,2])
print(ac.input('i'))
print(ac.input(' '))
print(ac.input('a'))
print(ac.input('#'))
print(ac.input('i'))
print(ac.input(' '))
print(ac.input('a'))
print(ac.input('#'))
print(ac.input('i'))
print(ac.input(' '))
print(ac.input('a'))
print(ac.input('#'))