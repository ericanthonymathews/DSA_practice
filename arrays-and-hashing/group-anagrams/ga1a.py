class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_groups = list()
        anagram_groups_dict = dict()
        for s in strs:
            sorted_group_name = ''.join(sorted(s))
            if sorted_group_name not in anagram_groups_dict:
                anagram_groups_dict[sorted_group_name] = [s]
            else:
                anagram_groups_dict[sorted_group_name].append(s)
        for key in anagram_groups_dict:
            anagram_groups.append(anagram_groups_dict[key])
        return anagram_groups
