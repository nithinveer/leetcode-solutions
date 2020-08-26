class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'
        lst = []
        singles = {
                0: '',
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
        tens = {
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen'
            }
        doubles = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }




        divs = ['Billion','Million','Thousand', '']
        while num > 0:
            lst.append(num%1000)
            num = int(num/1000)
        lst.reverse()
        def convert(value):
            rtn = []
            if int(value/100) > 0:
                if int(value/100) !=0:
                    rtn.append(singles[int(value/100)] )
                    rtn.append('Hundred')
            twos = value%100
            if 0< twos<= 9:
                rtn.append(singles[twos])
            elif 10 <= twos <= 19:
                rtn.append(tens[twos])
            elif 20 <= twos <= 99:
                rtn.append(doubles[int(twos/10)])
                if int(twos%10) !=0:
                    rtn.append(singles[int(twos%10)])
            return rtn
        piv = 4-len(lst)
        rtn = []
        for each in lst:
            tmp = convert(each)
            if tmp:
                rtn.extend(tmp)
                rtn.append(divs[piv])
            piv+=1
        ret = (" ".join(e for e in rtn))
        return ret.strip()



num =50868
sol = Solution()
print(sol.numberToWords(num))