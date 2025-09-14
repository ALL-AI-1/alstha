#this is the  standard trie tree. Less time compledxity but very memory inefficient.. (Computer Code)

class TrieNode:
    def __init__(self):
        # Each TrieNode represents a single character in the trie.
        # The root node is a special, empty node (does not store any character).
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        # The root node is the first node of the trie and is always empty.
        # It serves as the starting point for all insert and search operations.
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage and testing
if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "bat", "bath", "batman"]
    for word in words:
        trie.insert(word)

    print(trie.search("app"))      # True
    print(trie.search("apple"))    # True
    print(trie.search("bat"))      # True
    print(trie.search("bath"))     # True
    print(trie.search("batman"))   # True
    print(trie.search("batmobile"))# False
    print(trie.starts_with("bat")) # True
    print(trie.starts_with("ba"))  # True
    print(trie.starts_with("cat")) # False



# TST(Trie+BST) - little slower that standard trie but memory efficient.. (Computer Code)

class TSTNode:
    def __init__(self, char):
        self.char = char
        self.left = None
        self.eq = None
        self.right = None
        self.is_end_of_word = False

class TST:
    def __init__(self):
        self.root = None

    def insert(self, word):
        if not word:
            return
        self.root = self._insert(self.root, word, 0)

    def _insert(self, node, word, idx):
        char = word[idx]
        if node is None:
            node = TSTNode(char)
        if char < node.char:
            node.left = self._insert(node.left, word, idx)
        elif char > node.char:
            node.right = self._insert(node.right, word, idx)
        else:
            if idx + 1 < len(word):
                node.eq = self._insert(node.eq, word, idx + 1)
            else:
                node.is_end_of_word = True
        return node

    def search(self, word):
        return self._search(self.root, word, 0)

    def _search(self, node, word, idx):
        if not node or not word:
            return False
        char = word[idx]
        if char < node.char:
            return self._search(node.left, word, idx)
        elif char > node.char:
            return self._search(node.right, word, idx)
        else:
            if idx + 1 == len(word):
                return node.is_end_of_word
            return self._search(node.eq, word, idx + 1)

    def starts_with(self, prefix):
        return self._starts_with(self.root, prefix, 0)

    def _starts_with(self, node, prefix, idx):
        if not node or not prefix:
            return False
        char = prefix[idx]
        if char < node.char:
            return self._starts_with(node.left, prefix, idx)
        elif char > node.char:
            return self._starts_with(node.right, prefix, idx)
        else:
            if idx + 1 == len(prefix):
                return True
            return self._starts_with(node.eq, prefix, idx + 1)

# Example usage and testing for TST
if __name__ == "__main__":
    tst = TST()
    words = ["apple", "app", "bat", "bath", "batman"]
    for word in words:
        tst.insert(word)

    print(tst.search("app"))      # True
    print(tst.search("apple"))    # True
    print(tst.search("bat"))      # True
    print(tst.search("bath"))     # True
    print(tst.search("batman"))   # True
    print(tst.search("batmobile"))# False
    print(tst.starts_with("bat")) # True
    print(tst.starts_with("ba"))  # True
    print(tst.starts_with("cat")) # False


# WE can also use trie+heap (for Smart Suggestion on frequent searrch and also get the top-K search )

# Trie + Heap for Top-K Frequent Word Suggestions but no real time update (best for static data)

import heapq

class TrieNodeHeap:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.top_k_heap = []  # min-heap of (frequency, word)

class TrieHeap:
    def __init__(self, k=2):
        self.root = TrieNodeHeap()
        self.k = k  # top-k words per node

    def insert(self, word, freq):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNodeHeap()
            node = node.children[char]
            # Maintain top-k heap at this node
            heapq.heappush(node.top_k_heap, (freq, word))
            if len(node.top_k_heap) > self.k:
                heapq.heappop(node.top_k_heap)
        node.is_end_of_word = True

    def top_words(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        # Return heap sorted by frequency descending
        return sorted(node.top_k_heap, reverse=True)

# Example
trie_heap = TrieHeap(k=2)
trie_heap.insert("bat", 2)
trie_heap.insert("bath", 4)
trie_heap.insert("batman", 1)


print("Trie + Heap top words for 'bat':", trie_heap.top_words("bat"))
# Output: [('bath', 4), ('bat', 2)]
# Notice batman is NOT in top-2 even if frequency later increases



# Trie + Heap for Top-K Frequent Word Suggestions ( use for dynamic changing frequency of data)- realtime get the top-k result.


from queue import PriorityQueue

class TrieNodePQ:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.pq = PriorityQueue()  # priority queue to store (-frequency, word)
        self.freq_map = {}          # dictionary to track current frequency

class TriePQ:
    def __init__(self):
        self.root = TrieNodePQ()

    def insert(self, word, freq):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNodePQ()
            node = node.children[char]
            # Update frequency map
            node.freq_map[word] = freq
            # Push into priority queue (max-heap using negative frequency)
            node.pq.put((-freq, word))
        node.is_end_of_word = True

    def update_frequency(self, word, new_freq):
        node = self.root
        for char in word:
            node = node.children[char]
            node.freq_map[word] = new_freq
            # Push updated frequency into priority queue
            node.pq.put((-new_freq, word))

    def top_words(self, prefix, k=2):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        # Extract top-k unique words from priority queue
        seen = set()
        result = []
        temp = []

        while not node.pq.empty() and len(result) < k:
            freq, word = node.pq.get()
            freq = -freq  # convert back to positive
            if word in node.freq_map and node.freq_map[word] == freq and word not in seen:
                result.append((word, freq))
                seen.add(word)
            temp.append((-freq, word))  # store to push back

        # Push items back into priority queue
        for item in temp:
            node.pq.put(item)

        return result

# ---------------- Example Usage ----------------
trie_pq = TriePQ()
trie_pq.insert("bat", 2)
trie_pq.insert("bath", 4)
trie_pq.insert("batman", 1)

print("Before update, top words for 'bat':", trie_pq.top_words("bat"))
# [('bath', 4), ('bat', 2)]

# Update batman frequency
trie_pq.update_frequency("batman", 10)
print("After update, top words for 'bat':", trie_pq.top_words("bat"))
# [('batman', 10), ('bath', 4)]

# Insert a new word
trie_pq.insert("battery", 5)
print("Top words for 'bat':", trie_pq.top_words("bat"))
# [('batman', 10), ('battery', 5)]


