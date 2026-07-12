########    BRUTE FORCE APPROACH TIME COMPLEXITY O(nlogn)    ########

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dicct = {}
        res = []
        # calculate count of every number using dictionary
        for i in nums:
            dicct[i] = dicct.get(i, 0) + 1
        # sort dictonary
        sorted_items = sorted(dicct.items(), key=lambda x: x[1], reverse=True)
        for key, value in sorted_items:
            # append the res
            res.append(key)
            # check if len(res) == k break the loop
            if len(res) == k:
                break
        return res


######## OPTIMIZE APPROACH WITH BUCKET SORT TIME COMPLEXITY O(n)   #######


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # step 1 count frequency of every number
        # step 2 create a bucket of n+1 length
        # step 3  store the value of by frequency
        # step4 compute the result

        count = {}
        n = len(nums)
        # frequency count
        for i in nums:
            count[i] = count.get(i, 0) + 1

        # creating bucket
        bucket = [[] for i in range(n + 1)]

        # store the value in bucket
        for key, freq in count.items():
            bucket[freq].append(key)

        # compute result
        res = []
        for freq in range(len(bucket) - 1, 0, -1):
            for num in bucket[freq]:
                res.append(num)
                if len(res) == k:
                    return res




