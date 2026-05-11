class Solution:
    def longestCommonPrefix(self, strs):

        answer = ""

        # loop through letters of first word
        for i in range(len(strs[0])):

            current_letter = strs[0][i]
            # compare with all words
            for word in strs:
                # if letter is different or index too big
                if i >= len(word) or word[i] != current_letter:
                    break

            else:
                # if all letters matched
                answer = answer + current_letter
                continue
            # stop if letters are different
            break

        return answer