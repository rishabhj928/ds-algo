
# Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, 
# replace all the successors in the sentence with the root forming it. If a successor can be replaced by more than one root, 
# replace it with the root that has the shortest length.
# Return the sentence after the replacement.
# Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
# Output: "a a b c"

from typing import List
class TrieNode:
    def __init__(self):
        self.child = [None]*26
        self.word = ""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = TrieNode()
        for word in dictionary:
            cur = trie
            for letter in word:
                if cur.child[ord(letter)-ord('a')-1] is None:
                    cur.child[ord(letter)-ord('a')-1] = TrieNode()
                cur = cur.child[ord(letter) - ord('a') - 1]
            cur.word = word
        print(trie.child)
        ans = []
        for word in sentence.split(" "):
            cur = trie
            for letter in word:
                if cur.child[ord(letter)-ord('a')-1] is None or cur.word != "":
                    break
                cur = cur.child[ord(letter)-ord('a')-1]
            x = cur.word if cur.word else word
            ans.append(x)
        return " ".join(ans)

if __name__ == "__main__":
    s = Solution()
    test_cases = 3
    dc = [["cat","rat","bat"], ["a","b","c"], ['sun', 'sat', 'fri', 'thu', 'wed', 'tue', 'mon']]
    sn = ["the cattle was rattled by the battery", "aadsfasf absbs bbab cadsfafs", "monday tuesday wednesday thursday friday sunday saturday"]
    for i in range(test_cases):
        ans = s.replaceWords(dc[i], sn[i])
        print(ans)
