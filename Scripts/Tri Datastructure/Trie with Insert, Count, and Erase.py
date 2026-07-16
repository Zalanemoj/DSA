from os import *
from sys import *
from collections import *
from math import *

class TriNode:
    def __init__(self):
        self.children = {

        }
        self.word_end=0
        self.prefix=0

class Trie:
    def __init__(self):
        self.root = TriNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TriNode()
            curr = curr.children[c]
            curr.prefix+=1
        curr.word_end+=1

    def count_words_equal_to(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.word_end

    def word_start_with(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return 0
            curr = curr.children[c]
        return curr.prefix

    def erase(self,word):
        curr = self.root
        for char in word:
            if char in curr.children:
                curr.prefix-=1
            else:
                return
            curr = curr.children[char]
        curr.word_end-=1