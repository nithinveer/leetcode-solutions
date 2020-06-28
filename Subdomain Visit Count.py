class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dct = {}
        for each_ in cpdomains:
            cnt, stg = each_.split()
            tmp_domains = stg.split('.')
            for i in range(len(tmp_domains)):
                tmp = ".".join(tmp_domains[i:])
                if tmp not in dct:
                    dct[tmp] = int(cnt)
                else:
                    dct[tmp] += int(cnt)


        rtn = []
        for each_ in dct.keys():
            rtn.append(str(dct[each_]) + " "+ each_ )

        return rtn




sol = Solution()
cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
print(sol.subdomainVisits(cpdomains))
