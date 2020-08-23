class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        hex ='0123456789abcdefABCDEF'
        hexset = set()
        for each in hex:
            hexset.add(each)
        tmp = IP.split('.')
        if len(IP.split('.')) == 4:
            # IPV4
            tmp = IP.split('.')
            for each in tmp:
                if len(each) > 3 or len(each) == 0:
                    return "Neither"
                if each[0] == '0' and len(each) != 1:
                    return "Neither"
                if each.isdigit() and 0 <= int(each) <= 255:
                    continue
                else:
                    return "Neither"

            return "IPv4"

        elif len(IP.split(':')) == 8:
            tmp = IP.split(':')
            for each in tmp:
                if 1<=len(each)<=4 and all(c in hexset for c in each):
                    continue
                else:
                    return "Neither"
            return "IPv6"
        else:
            return "Neither"




sol = Solution()
IP =  "1e1.4.5.6"
print(sol.validIPAddress(IP))