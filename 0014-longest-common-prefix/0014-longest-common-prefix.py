class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            sym = strs[0][i]
            for s in strs:                
                try:
                    if s[i] != sym:
                        return strs[0][:i]
                except IndexError:
                    return strs[0][:i]
        return strs[0]