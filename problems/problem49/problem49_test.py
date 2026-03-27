import unittest

from problem49 import Solution

class Test49Solution(unittest.TestCase):
    def test_example1(self):
        strs = ["eat","tea","tan","ate","nat","bat"]
        result = Solution().groupAnagrams(strs)
        target = [["bat"],["nat","tan"],["ate","eat","tea"]]
        self.assertEqual(result, target)

    def test_example2(self):
        strs = [""]
        result = Solution().groupAnagrams(strs)
        target = [[""]]
        self.assertEqual(result, target)

    def test_example3(self):
        strs = ["a"]
        result = Solution().groupAnagrams(strs)
        target = [["a"]]
        self.assertEqual(result, target)

if __name__ == "__main__":
    unittest.main()
