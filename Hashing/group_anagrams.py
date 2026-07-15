
########  APPROACH WITH SORTING  ########

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        res = []
        # iterate through each element
        # sort the element and store that in freq as key
        # store the value as original value
        # as last fetch data from freq and add it res list
        for i in strs:
            # if not freq:
            #     freq[''.join(sorted(i))] = [i]
            srt = ''.join(sorted(i))
            if srt not in freq:
                freq[srt] = [i]

            elif srt in freq:
                freq[srt].append(i)
        for key, value in freq.items():
            res.append(value)

        return res

########  APPROACH WITHOUT SORTING  ##########















