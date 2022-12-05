
# given a list of product names, return the related products when searchword is typed char by char
# e.g. ['bat', 'bar', 'bee', 'ben']
# search - 

from collections import defaultdict
from typing import List
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.suggestion = []
    def add_suggestion(self, product):
        if len(self.suggestion) < 3:
            self.suggestion.append(product)

def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    products.sort()
    root = TrieNode()
    for p in products:
        node = root
        for char in p:
            node = node.children[char]
            node.add_suggestion(p)
    result, node = [], root
    for char in searchWord:
        node = node.children[char]
        result.append(node.suggestion)
    return result

print(suggestedProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
# print(suggestedProducts(["havana"], "havana"))
# print(suggestedProducts(["bags","baggage","banner","box","cloths"], "bags"))
