def heap_sort (sequence):
    def sift_down (parent, limit):
        item = sequence[parent]
        while True:
            child = (parent << 1) + 1
            if child >= limit:
                break
            if child + 1 < limit and sequence[child] < sequence[child + 1]:
                child += 1
            if item < sequence[child]:
                sequence[parent] = sequence[child]
                parent = child
            else:
                break
        sequence[parent] = item
    length = len(sequence)
    for index in range((length >> 1) - 1, -1, -1):
        sift_down(index, length)
    for index in range(length - 1, 0, -1):
        sequence[0], sequence[index] = sequence[index], sequence[0]
        sift_down(0, index)
count = 10
sequence = list(range(count, 0, -1))
print("Исходная последовательность:")
print(sequence)
heap_sort(sequence)
print("Упорядоченная последовательность:")
print(sequence)