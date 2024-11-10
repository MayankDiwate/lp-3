import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, data, frequency):
        self.data = data
        self.frequency = frequency
        self.left = None
        self.right = None

    # Comparison function for priority queue
    def __lt__(self, other):
        return self.frequency < other.frequency

def print_codes(root, code):
    if root is None:
        return
    if root.data != '\0':
        print(f"{root.data}: {code}")
    print_codes(root.left, code + "0")
    print_codes(root.right, code + "1")

def huffman_encoding(input_string):
    # Step 1: Calculate frequencies
    frequency_map = defaultdict(int)
    for c in input_string:
        frequency_map[c] += 1

    # Step 2: Create priority queue (min-heap) and populate it with initial nodes
    priority_queue = [HuffmanNode(data, frequency) for data, frequency in frequency_map.items()]
    heapq.heapify(priority_queue)

    # Step 3: Build the Huffman Tree
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode('\0', left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    # Root node of the Huffman Tree
    root = priority_queue[0]

    # Step 4: Print Huffman Codes
    print("Huffman Codes:")
    print_codes(root, "")

if __name__ == "__main__":
    input_string = input("Enter a string: ")
    huffman_encoding(input_string)
