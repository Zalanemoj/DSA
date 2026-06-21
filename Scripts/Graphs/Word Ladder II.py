from collections import deque
from typing import List

class Solution:
    """This class deals with the solution of world ladder problem"""

    def solve(self,begin_word:str,end_word:str,word_list:List[str],result:List[str])->None:
        """This function deals with solving of the problem"""
        # Converting list into set in order to reduce the time complexity
        word_set=set(word_list)

        # Initializing the queue
        queue = deque()
        queue.append([begin_word])

        while queue:
            level_size = len(queue)
            chosen_word = set()

            # Iterating through all the items in the given level
            for _ in range(level_size):
                sequence = queue.popleft()
                last_word = sequence[-1]

                # If the last word equals to the end word then sequence is over
                if last_word == end_word:
                    result.append(sequence)

                # Iterate through the word
                for i in range(len(last_word)):
                    # Iterate through each and every character of the English alphabet in order to get the suitable result for a particular position
                    for character in "abcdefghijklmnopqrstuvwxyz":
                        #  If the ith index and the character are same that means the word is not changed so continue
                        if last_word[i] == character:
                            continue

                        # New word
                        new_word = last_word[:i] + character + last_word[i+1:]

                        if new_word in word_set:
                            # New sequence after that appending the word to the sequence
                            new_sequence = sequence + [new_word]
                            # Appending the new sequence to the Q
                            queue.append(new_sequence)
                            # Adding the new word to the chosen word so that we can remove it after the loops get end
                            chosen_word.add(new_word)

            # Removing the element after the loops get over from the word set
            for w in chosen_word:
                word_set.remove(w)

    def word_ladder_two(self)->List[str]:
        """These function deals with initializing and declaring all the variables that are required"""
        begin_word = "hit"
        end_word = "cog"
        word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
        result = []

        # Calling of the function
        self.solve(begin_word,end_word,word_list,result)

        # Returning of the result
        if end_word not in word_list:
            return []

        return result

#region Printing_result
sol = Solution()
print(sol.word_ladder_two())
#endregion

#region Complexity
# Time -> o(n) + o(26*n*n)
#         Conversion to set + for loops

# Space -> o(n) + o(n)
#          Storing of the result variable + Max Stack Space

#endregion