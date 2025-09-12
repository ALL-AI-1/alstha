import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        heapq.heappush(self.heap, item)
    
    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def heapify(self, arr):
        heapq.heapify(arr)
        self.heap = arr

class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def push(self, item):
        # Negate the item to simulate max heap behavior
        heapq.heappush(self.heap, -item)
    
    def pop(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        return None
    
    def peek(self):
        if self.heap:
            return -self.heap[0]
        return None
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def heapify(self, arr):
        # Negate all elements for max heap behavior
        negated_arr = [-x for x in arr]
        heapq.heapify(negated_arr)
        self.heap = negated_arr

class HeapNode:
    def __init__(self, value, priority=None):
        self.value = value
        self.priority = priority if priority is not None else value
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __eq__(self, other):
        return self.priority == other.priority
    
    def __repr__(self):
        return f"HeapNode({self.value}, {self.priority})"

class PriorityQueue:
    def __init__(self):
        self.heap = []
    
    def enqueue(self, item, priority):
        node = HeapNode(item, priority)
        heapq.heappush(self.heap, node)
    
    def dequeue(self):
        if self.heap:
            return heapq.heappop(self.heap).value
        return None
    
    def peek(self):
        if self.heap:
            return self.heap[0].value
        return None
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)

# Example usage and testing
if __name__ == "__main__":
    print("=== Min Heap Example ===")
    min_heap = MinHeap()
    elements = [3, 1, 4, 1, 5, 9, 2, 6]
    for elem in elements:
        min_heap.push(elem)
    
    print("Min heap elements:", min_heap.heap)
    print("Peek (min):", min_heap.peek())
    print("Pop:", min_heap.pop())
    print("After pop:", min_heap.heap)
    
    print("\n=== Max Heap Example ===")
    max_heap = MaxHeap()
    for elem in elements:
        max_heap.push(elem)
    
    print("Max heap elements:", max_heap.heap)
    print("Peek (max):", max_heap.peek())
    print("Pop:", max_heap.pop())
    print("After pop:", max_heap.heap)
    
    print("\n=== Priority Queue Example ===")
    pq = PriorityQueue()
    tasks = [("Task A", 3), ("Task B", 1), ("Task C", 2), ("Task D", 1)]
    for task, priority in tasks:
        pq.enqueue(task, priority)
    
    print("Processing tasks by priority:")
    while not pq.is_empty():
        print(pq.dequeue())

