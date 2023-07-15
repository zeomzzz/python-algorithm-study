class Node(object):
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}

class Trie(object):
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur_node = self.head

        for char in string:
            if char not in cur_node.children: cur_node.children[char] = Node(char)
            cur_node = cur_node.children[char]

        cur_node.data = string

    def search(self, string):
        cur_node = self.head

        for char in string:
            if char in cur_node.children: cur_node = cur_node.children[char]
            else: return False
            
        if cur_node.data: return True
        
        return False


import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trie = Trie()
cnt = 0

for i in range(N) :
    string = input().rstrip()
    trie.insert(string)

for i in range(M) :
    string = input().rstrip()
    if trie.search(string) : cnt += 1

print(cnt)
