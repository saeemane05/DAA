# Huffman Encoding

def make_codes(node, code):
    if node[2] == None and node[3] == None:
        print(node[1], ":", code)
        return

    make_codes(node[2], code + "0")
    make_codes(node[3], code + "1")


# Input
characters = input("Enter characters: ")

frequencies = input("Enter frequencies separated by space: ")
frequencies = frequencies.split()

nodes = []

for i in range(len(characters)):
    frequency = int(frequencies[i])

    node = [frequency, characters[i], None, None]
    nodes.append(node)


# Build Huffman Tree
while len(nodes) > 1:

    nodes.sort()

    left = nodes.pop(0)
    right = nodes.pop(0)

    total = left[0] + right[0]

    parent = [total, "", left, right]

    nodes.append(parent)


# Display Codes
print("Huffman Codes:")
make_codes(nodes[0], "")