"""
208-实现 Trie (前缀树)(implement-trie-prefix-tree)
"""


# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
# 
#  示例: 
# 
#  Trie trie = new Trie();
# 
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");   
# trie.search("app");     // 返回 true 
# 
#  说明: 
# 
#  
#  你可以假设所有的输入都是由小写字母 a-z 构成的。 
#  保证所有输入均为非空字符串。 
#  
#  Related Topics 设计 字典树 
#  👍 538 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Trie(object):
    class TrieNode(object):

        def __init__(self, token=None):
            self.token = token
            self.children_nodes = {}
            self.is_word = False
            pass

        pass

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children_nodes = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        children_nodes = self.children_nodes
        trie_node = None
        for c in word:
            if c not in children_nodes.keys():
                # 不存在节点
                trie_node = self.TrieNode(c)
                children_nodes[c] = trie_node
                pass
            else:
                # 已存在节点
                trie_node = children_nodes[c]
                pass
            # 向下移动
            children_nodes = trie_node.children_nodes
        if isinstance(trie_node, self.TrieNode):
            trie_node.is_word = True
            pass

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        ret_val = False
        if self.children_nodes:
            children_nodes = self.children_nodes
            trie_node = None
            for c in word:
                if c in children_nodes.keys():
                    trie_node = children_nodes[c]
                    children_nodes = trie_node.children_nodes
                    pass
                else:
                    return False
                pass
            pass
            if isinstance(trie_node, self.TrieNode) and trie_node.is_word:
                ret_val = True
        return ret_val

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ret_val = False
        if self.children_nodes:
            children_nodes = self.children_nodes
            trie_node = None
            for c in prefix:
                if c in children_nodes.keys():
                    trie_node = children_nodes[c]
                    children_nodes = trie_node.children_nodes
                    pass
                else:
                    return False
                pass
            if isinstance(trie_node, self.TrieNode):
                ret_val = True
            pass
        return ret_val


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# leetcode submit region end(Prohibit modification and deletion)


def app():
    l_temp = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    obj = Trie()
    for item in l_temp:
        obj.insert(item)
        pass
    print()
    l_tst = [[], ["hello"], ["hell"], ["helloa"], ["hello"], ["hell"], ["helloa"], ["hello"]]
    for item in l_tst:
        for t in item:
            if t:
                print(f"word: {t}")
                a = obj.search(t)
                b = obj.startsWith(t)
                print(f"search: {a}")
                print(f"starts: {b}")
                obj.insert(t)
                print()
    pass


if __name__ == '__main__':
    app()
