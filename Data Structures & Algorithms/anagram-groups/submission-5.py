class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counts = {}

        for s in strs:
            key = "".join(sorted(s))
            if key in counts:
                counts[key].append(s)
            else:
                counts[key] = [];
                counts[key].append(s)
        
        return list(counts.values())