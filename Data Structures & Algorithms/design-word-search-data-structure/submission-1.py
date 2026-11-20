class WordDictionary:

    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def addWord(self, word: str) -> None:
        node = self
        for char in word:
            if char not in node.children:
                node.children[char] = WordDictionary()
            node = node.children[char]
        node.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(self, i):
            node = self
            if i == len(word):
                return node.endOfWord
            
            char = word[i]
            if char == '.':
                for child in node.children.values():
                    if dfs(child, i + 1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return dfs(node.children[char], i + 1)

        return dfs(self, 0)

