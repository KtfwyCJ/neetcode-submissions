class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            stored_words = "".join(sorted(word))
            groups[stored_words].append(word)

        return list(groups.values())
        