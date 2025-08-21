class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_map = {}
        for i in range(len(strs)):
            alpha_count = [0]*26
            for j in strs[i]:
                alpha_count[ord(j)-97]+=1
            if (str(alpha_count) in count_map):
                count_map[str(alpha_count)].append(strs[i])
            else:
                count_map[str(alpha_count)] = [strs[i]]
        return list(count_map.values())