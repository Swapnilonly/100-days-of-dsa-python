class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        check = [False] * 1000
        n = len(digits)
        res = 0
        for i in range(n):
            if digits[i] == 0:
                continue

            for j in range(n):
                if i == j:
                    continue

                for k in range(n):
                    if i == k or j == k or digits[k] % 2 != 0:
                        continue
                    num = digits[i] * 100 + digits[j] * 10 + digits[k]
                    if not check[num]:
                        res += 1
                        check[num] = True
        return res
