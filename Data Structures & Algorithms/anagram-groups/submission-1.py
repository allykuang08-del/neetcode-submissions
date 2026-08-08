class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = {}

        for s in strs:
            count = [0] * 26
            for char in s:
                row = ord(char) - ord('a')
                count[row] += 1
        
            key = tuple(count)
            if key not in result:
                result[key] = []
            result[key].append(s)


        return list(result.values())