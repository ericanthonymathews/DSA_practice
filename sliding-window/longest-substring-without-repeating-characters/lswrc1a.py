class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # all_current_characters = (a)
        # max_count = 0
        # l = 0
        # r = 0
        # abcabcbb
        # l
        # r
        if not s:
            return 0
        if s == "":
            return 0
        max_count = 1
        l = 0
        r = 0
        all_current_characters = set()

        while r <= len(s) - 1:
            left_character = s[l]
            right_character = s[r]
            if l == r:
                r += 1
            if right_character in all_current_characters:
                l += 1
                all_current_characters.remove(right_character)
            else:
                all_current_characters.add(right_character)
            if r - l - 1 > max_count:
                max_count = r - l - 1
            r += 1
        return max_count

        # set a count for the longest substring
        # iterate through the string
        # instantiate a set
        # if the string repeats a character
        # if the count is greater
        # replace the count
        # otherwise we should add the current letter to the new set and
        # increase the count
        # we check if the final count is greater than the current count
        # we replace that count
        # return the greatest string count without repeating characters

        # "abcabcbb"
        # max_count = 3

        # set= ()
        # abcabcbb
        # ^^
        #
        # set = ()
        # abcabcbb
        # ^
        # pwwkew
        #   lr

        # for left in range(len(str) - 1):
        #     current_letters = set()
        #     for right in range(1, len(str)):
        #         if str[right] in current_letters:
        #             if right - left > max_count:
        #                 max_count = right - left
        #             left += 1
        #             right += 1
        #         else:
        #             current_letters.add(str[right])
