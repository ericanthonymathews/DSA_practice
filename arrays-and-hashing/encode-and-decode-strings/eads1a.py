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
        for str in strs:
            res += str(len(s)) + '#' + str
        return res

    def decode(self, str):
        """Decodes the string into a list of strings

        Args:
            str (string): encoded string to be decoded
        Returns:
            list: list of strings contained within the encoded string
        """
        res, i = [], 0
        while i < len(str):
            j = i
            while j != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
