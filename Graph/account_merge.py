
from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node: int) -> int:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])

        return self.parent[node]

    def union_by_size(self, first: int, second: int) -> None:
        root_first = self.find(first)
        root_second = self.find(second)

        if root_first == root_second:
            return

        if self.size[root_first] < self.size[root_second]:
            root_first, root_second = root_second, root_first

        self.parent[root_second] = root_first
        self.size[root_first] += self.size[root_second]


class Solution:
    def accountsMerge(
        self, accounts: List[List[str]]
    ) -> List[List[str]]:
        account_count = len(accounts)
        dsu = DSU(account_count)
        mail_to_node = {}

        # Step 1: Connect accounts sharing an email.
        for account_index, account in enumerate(accounts):
            for email in account[1:]:
                if email in mail_to_node:
                    dsu.union_by_size(
                        account_index, mail_to_node[email]
                    )
                else:
                    mail_to_node[email] = account_index

        # Step 2: Group emails by their component's root.
        merged_mail = [[] for _ in range(account_count)]

        for email, account_index in mail_to_node.items():
            root = dsu.find(account_index)
            merged_mail[root].append(email)

        # Step 3: Sort emails and construct the result.
        result = []

        for account_index, emails in enumerate(merged_mail):
            if not emails:
                continue

            emails.sort()
            name = accounts[account_index][0]
            result.append([name] + emails)

        return result
