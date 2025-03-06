class Trie:
    def __init__(self):
        self.root = {}
        self.end = -1
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.end] = True
        
    def search(self, word):
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end in node
    
def main():
    trie = Trie()
    trie.insert("apple")
    trie.insert("app")
    trie.insert("apricot")
    trie.insert("banana")
    trie.insert("cherry")
    print(trie.search("apple"))    # True
    print(trie.search("app"))      # True
    print(trie.search("apricot"))  # True
    print(trie.search("banana"))   # True
    print(trie.search("cherry"))   # True
    print(trie.search("ap"))       # False
    print(trie.search("apricots")) # False
    
if __name__ == "__main__":
    main()