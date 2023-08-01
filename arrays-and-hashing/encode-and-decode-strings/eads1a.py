class Solution:
    def encode(self, strs):
        """Encodes the list of strings into a single string with the following sequence:
          '2#be4#cool5#buddy'
          <int: string length><str: hashtag symbol to denote end of int string><str: encoded str>...

        Args:
            strs (list): list of strings

        Returns:
            string: encoded string containing strings from list
        """
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s):
        """Decodes the string into a list of strings

        Args:
            s (string): encoded string to be decoded
        Returns:
            list: list of strings contained within the encoded string
        """
        res, i = [], 0
        while i < len(s):
            j = i
            while j != '#':
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
