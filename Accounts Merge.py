from collections import defaultdict


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        visited_accounts = [False] * len(accounts)
        emails_accounts_map = defaultdict(list)
        res = []
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                emails_accounts_map[account[j]].append(i)

        # DFS code for traversing accounts.
        def dfs(i, emails):
            if visited_accounts[i]:
                return
            visited_accounts[i] = True
            for j in range(1, len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in emails_accounts_map[email]:
                    dfs(neighbor, emails)

        # Perform DFS for accounts and add to results.
        for i, account in enumerate(accounts):
            if visited_accounts[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            res.append([name] + sorted(emails))
        return res


accounts = [["David", "David0@m.co", "David1@m.co"], ["David", "David3@m.co", "David4@m.co"],
            ["David", "David4@m.co", "David5@m.co"], ["David", "David2@m.co", "David3@m.co"],
            ["David", "David1@m.co", "David2@m.co"]]
sol = Solution()
print(sol.accountsMerge(accounts))
