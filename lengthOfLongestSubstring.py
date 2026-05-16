def lengthOfLongestSubstring(s: str) -> int:
        longest_strings = []
        for index, char in enumerate(s):
            if not s:
                return 0
            orginal_char = char
            temp_char = ""
            temp_index = index
            temp_word = orginal_char
            while orginal_char != temp_char:
                temp_index += 1
                if temp_index >= len(s):
                    break
                temp_char = s[temp_index]
                if temp_char == orginal_char:
                    break
                print(temp_char)
                if temp_char in temp_word:
                    break
                temp_word += temp_char
            longest_strings.append(len(temp_word))

        return max(longest_strings)
