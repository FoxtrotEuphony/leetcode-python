from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_list: list[list[int]] = []
        grouped: list[list[str]] = []
        for word in strs:
            count = self.letter_count(word)
            for i, cl in enumerate(count_list):
                if cl == count:
                    grouped[i].append(word)
                    break
            else:
                count_list.append(count)
                grouped.append([word])
        return grouped

                    


    def letter_count(self, s: str) -> list[int]:
        count_array = [0 for _ in range(26)]
        for char in s:
            index = ord(char) - 97
            count_array[index] += 1
        return count_array
        
