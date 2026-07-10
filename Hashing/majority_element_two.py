## TIME COMPLEXITY O(n)
## SPACE COMPLEXITY O(n)


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 1 start a loop
        # 2 store the frequency of the number in a dict
        # 3 iterate through the loop with given condition
        check = {}
        n = len(nums)
        res = []
        m = n // 3
        for i in range(n):
            check[nums[i]] = check.get(nums[i], 0) + 1
        for key, value in check.items():
            if check[key] > m:
                res.append(key)
        return res


#####    Boyer-Moore Voting Algorithm Extended Version   ########


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Step 1: Find two possible candidates
        cand1 = None
        cand2 = None
        count1 = 0
        count2 = 0

        for num in nums:

            if num == cand1:
                count1 += 1

            elif num == cand2:
                count2 += 1

            elif count1 == 0:
                cand1 = num
                count1 = 1

            elif count2 == 0:
                cand2 = num
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify the candidates
        count1 = 0
        count2 = 0

        for num in nums:
            if num == cand1:
                count1 += 1
            elif num == cand2:
                count2 += 1

        # Step 3: Prepare answer
        ans = []

        if count1 > len(nums) // 3:
            ans.append(cand1)

        if count2 > len(nums) // 3:
            ans.append(cand2)

        return ans






