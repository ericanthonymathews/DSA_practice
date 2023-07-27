class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            letters_dict = dict()
            for letter in s:
                if letter not in letters_dict:
                    letters_dict[letter] = 1
                else:
                    letters_dict[letter] += 1
            for letter in t:
                if letter not in letters_dict:
                    return False
                elif letters_dict[letter] == 1:
                    del letters_dict[letter]
                else:
                    letters_dict[letter] -= 1
            return True
